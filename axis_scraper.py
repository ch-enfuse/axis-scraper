 #!/usr/bin/env python3
"""
Axis Communications Product Scraper
Scrapes product datasheets and extracts SoC model and memory information
"""

import requests
import time
import json
import re
import logging
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
from dataclasses import dataclass
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('axis_scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class ProductInfo:
    """Data class for product information"""
    product_name: str
    product_url: str
    datasheet_url: str = ""
    soc_model: str = ""
    memory: str = ""
    category: str = ""
    collection: str = ""
    series: str = ""

class AxisScraper:
    def __init__(self, base_url: str = "https://www.axis.com", delay_range: tuple = (1, 3)):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.delay_range = delay_range
        self.products = []
        
    def _delay(self):
        """Add random delay between requests"""
        time.sleep(random.uniform(*self.delay_range))
        
    def _make_request(self, url: str, max_retries: int = 3) -> Optional[requests.Response]:
        """Make HTTP request with retry logic"""
        for attempt in range(max_retries):
            try:
                self._delay()
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                logger.warning(f"Request failed (attempt {attempt + 1}/{max_retries}): {url} - {e}")
                if attempt == max_retries - 1:
                    logger.error(f"Failed to fetch {url} after {max_retries} attempts")
                    return None
                time.sleep(2 ** attempt)  # Exponential backoff
        return None
    
    def _parse_html(self, response: requests.Response) -> Optional[BeautifulSoup]:
        """Parse HTML response"""
        try:
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Failed to parse HTML: {e}")
            return None
    
    def get_main_categories(self) -> List[Dict[str, str]]:
        """Get main product categories from the products page"""
        url = f"{self.base_url}/en-us/products"
        logger.info(f"Fetching main categories from: {url}")
        
        response = self._make_request(url)
        if not response:
            return []
        
        soup = self._parse_html(response)
        if not soup:
            return []
        
        categories = []
        # Find the products collection container
        products_collection = soup.find('div', class_='products-collection')
        if not products_collection:
            logger.error("Could not find products collection container")
            return []
        
        # Find all category links
        category_links = products_collection.find_all('a', class_='nav-card')
        
        for link in category_links:
            href = link.get('href')
            title_element = link.find('h4')
            
            if href and title_element:
                category_name = title_element.get_text(strip=True)
                category_url = urljoin(self.base_url, href)
                categories.append({
                    'name': category_name,
                    'url': category_url
                })
                logger.info(f"Found category: {category_name}")
        
        return categories
    
    def get_collections_in_category(self, category_url: str, category_name: str) -> List[Dict[str, str]]:
        """Get collections within a category"""
        logger.info(f"Fetching collections from category: {category_name}")
        
        response = self._make_request(category_url)
        if not response:
            return []
        
        soup = self._parse_html(response)
        if not soup:
            return []
        
        collections = []
        # Find collections within the category
        collections_container = soup.find('div', class_='views-element-container')
        if not collections_container:
            logger.warning(f"No collections container found for {category_name}")
            return []
        
        collection_links = collections_container.find_all('a', class_='nav-card')
        
        for link in collection_links:
            href = link.get('href')
            title_element = link.find('h4')
            
            if href and title_element:
                collection_name = title_element.get_text(strip=True)
                collection_url = urljoin(self.base_url, href)
                collections.append({
                    'name': collection_name,
                    'url': collection_url,
                    'category': category_name
                })
                logger.info(f"Found collection: {collection_name}")
        
        return collections
    
    def get_series_in_collection(self, collection_url: str, collection_name: str, category_name: str) -> List[Dict[str, str]]:
        """Get product series within a collection"""
        logger.info(f"Fetching series from collection: {collection_name}")
        
        response = self._make_request(collection_url)
        if not response:
            return []
        
        soup = self._parse_html(response)
        if not soup:
            return []
        
        series_list = []
        # Find series within the collection
        series_container = soup.find('div', class_='views-element-container')
        if not series_container:
            logger.warning(f"No series container found for {collection_name}")
            return []
        
        series_links = series_container.find_all('a', class_='nav-card')
        
        for link in series_links:
            href = link.get('href')
            title_element = link.find('h4')
            
            if href and title_element:
                series_name = title_element.get_text(strip=True)
                series_url = urljoin(self.base_url, href)
                series_list.append({
                    'name': series_name,
                    'url': series_url,
                    'collection': collection_name,
                    'category': category_name
                })
                logger.info(f"Found series: {series_name}")
        
        return series_list
    
    def get_products_in_series(self, series_url: str, series_name: str, collection_name: str, category_name: str) -> List[ProductInfo]:
        """Get individual products within a series"""
        logger.info(f"Fetching products from series: {series_name}")
        
        response = self._make_request(series_url)
        if not response:
            return []
        
        soup = self._parse_html(response)
        if not soup:
            return []
        
        products = []
        
        # Check if this is a series page with multiple products or a single product page
        product_links = soup.find_all('a', class_='nav-card')
        
        if product_links:
            # Multiple products in series
            for link in product_links:
                href = link.get('href')
                title_element = link.find('h4')
                
                if href and title_element:
                    product_name = title_element.get_text(strip=True)
                    product_url = urljoin(self.base_url, href)
                    
                    product_info = ProductInfo(
                        product_name=product_name,
                        product_url=product_url,
                        category=category_name,
                        collection=collection_name,
                        series=series_name
                    )
                    products.append(product_info)
                    logger.info(f"Found product: {product_name}")
        else:
            # This might be a single product page
            title_element = soup.find('h1')
            if title_element:
                product_name = title_element.get_text(strip=True)
                product_info = ProductInfo(
                    product_name=product_name,
                    product_url=series_url,
                    category=category_name,
                    collection=collection_name,
                    series=series_name
                )
                products.append(product_info)
                logger.info(f"Found single product: {product_name}")
        
        return products
    
    def get_datasheet_url(self, product: ProductInfo) -> str:
        """Get datasheet PDF URL from product support page"""
        support_url = f"{product.product_url}/support"
        logger.info(f"Fetching datasheet for: {product.product_name}")
        
        response = self._make_request(support_url)
        if not response:
            return ""
        
        soup = self._parse_html(response)
        if not soup:
            return ""
        
        # Find the datasheet section
        datasheet_section = soup.find('h2', string='Datasheet')
        if not datasheet_section:
            # Try alternative selectors
            datasheet_section = soup.find('h2', string=re.compile(r'Datasheet', re.IGNORECASE))
        
        if datasheet_section:
            # Find the download link in the datasheet section
            section_parent = datasheet_section.find_parent('li', class_='item-list')
            if section_parent:
                download_link = section_parent.find('a', class_='downloads-list__download-button')
                if download_link:
                    href = download_link.get('href')
                    if href:
                        datasheet_url = urljoin(self.base_url, href)
                        logger.info(f"Found datasheet: {datasheet_url}")
                        return datasheet_url
        
        logger.warning(f"No datasheet found for {product.product_name}")
        return ""
    
    def download_and_parse_pdf(self, pdf_url: str, product_name: str) -> Dict[str, str]:
        """Download PDF and extract SoC model and memory information"""
        logger.info(f"Downloading and parsing PDF for: {product_name}")
        
        try:
            response = self._make_request(pdf_url)
            if not response:
                return {"soc_model": "", "memory": ""}
            
            # Save PDF temporarily
            pdf_path = Path(f"temp_{product_name.replace(' ', '_')}.pdf")
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            
            # Parse PDF
            extracted_info = self._extract_from_pdf(pdf_path)
            
            # Clean up temporary file
            pdf_path.unlink(missing_ok=True)
            
            return extracted_info
            
        except Exception as e:
            logger.error(f"Failed to download/parse PDF for {product_name}: {e}")
            return {"soc_model": "", "memory": ""}
    
    def _extract_from_pdf(self, pdf_path: Path) -> Dict[str, str]:
        """Extract SoC model and memory from PDF using PyMuPDF"""
        soc_model = ""
        memory = ""
        
        try:
            doc = fitz.open(pdf_path)
            text = ""
            
            # Extract text from all pages
            for page in doc:
                text += page.get_text()
            
            doc.close()
            
            # Patterns to find SoC model
            soc_patterns = [
                r'SoC[:\s]*([A-Z0-9-]+)',
                r'System on Chip[:\s]*([A-Z0-9-]+)',
                r'Processor[:\s]*([A-Z0-9-]+)',
                r'ARTPEC[:\s-]*([0-9]+)',
                r'Chipset[:\s]*([A-Z0-9-]+)'
            ]
            
            for pattern in soc_patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    soc_model = match.group(1).strip()
                    if 'ARTPEC' in pattern:
                        soc_model = f"ARTPEC-{soc_model}"
                    break
            
            # Patterns to find memory
            memory_patterns = [
                r'Memory[:\s]*([0-9]+\s*[GM]B\s*RAM)',
                r'RAM[:\s]*([0-9]+\s*[GM]B)',
                r'System Memory[:\s]*([0-9]+\s*[GM]B)',
                r'([0-9]+\s*[GM]B)\s*RAM',
                r'([0-9]+\s*[GM]B)\s*memory'
            ]
            
            for pattern in memory_patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    memory = match.group(1).strip()
                    break
            
            logger.info(f"Extracted - SoC: {soc_model}, Memory: {memory}")
            
        except Exception as e:
            logger.error(f"Failed to extract from PDF {pdf_path}: {e}")
        
        return {"soc_model": soc_model, "memory": memory}
    
    def scrape_all_products(self, limit_categories: int = None, limit_collections: int = None) -> List[Dict]:
        """Main method to scrape all products"""
        logger.info("Starting full product scrape")
        
        # Get main categories
        categories = self.get_main_categories()
        if limit_categories:
            categories = categories[:limit_categories]
        
        all_products = []
        
        for category in categories:
            # Focus on Network Cameras first as per example
            if "Network cameras" not in category['name']:
                continue
                
            logger.info(f"Processing category: {category['name']}")
            
            # Get collections in category
            collections = self.get_collections_in_category(category['url'], category['name'])
            if limit_collections:
                collections = collections[:limit_collections]
            
            for collection in collections:
                logger.info(f"Processing collection: {collection['name']}")
                
                # Get series in collection
                series_list = self.get_series_in_collection(
                    collection['url'], 
                    collection['name'], 
                    collection['category']
                )
                
                for series in series_list:
                    logger.info(f"Processing series: {series['name']}")
                    
                    # Get products in series
                    products = self.get_products_in_series(
                        series['url'],
                        series['name'],
                        series['collection'],
                        series['category']
                    )
                    
                    for product in products:
                        # Get datasheet URL
                        product.datasheet_url = self.get_datasheet_url(product)
                        
                        if product.datasheet_url:
                            # Extract info from PDF
                            pdf_info = self.download_and_parse_pdf(
                                product.datasheet_url, 
                                product.product_name
                            )
                            product.soc_model = pdf_info["soc_model"]
                            product.memory = pdf_info["memory"]
                        
                        # Convert to dict for output
                        product_dict = {
                            "product": product.product_name,
                            "product_url": product.product_url,
                            "datasheet_url": product.datasheet_url,
                            "soc_model": product.soc_model,
                            "memory": product.memory,
                            "category": product.category,
                            "collection": product.collection,
                            "series": product.series
                        }
                        
                        all_products.append(product_dict)
                        logger.info(f"Completed product: {product.product_name}")
                        
                        # Save progress periodically
                        if len(all_products) % 10 == 0:
                            self.save_results(all_products, "progress_results.json")
        
        return all_products
    
    def save_results(self, products: List[Dict], filename: str = "axis_products.json"):
        """Save results to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(products, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved {len(products)} products to {filename}")
        except Exception as e:
            logger.error(f"Failed to save results: {e}")

def main():
    """Main execution function"""
    scraper = AxisScraper()
    
    # Start with a limited scrape for testing
    logger.info("Starting Axis Communications product scraper")
    
    try:
        # Scrape products (limit for testing)
        products = scraper.scrape_all_products(limit_categories=1, limit_collections=2)
        
        # Save final results
        scraper.save_results(products, "axis_products_final.json")
        
        logger.info(f"Scraping completed. Found {len(products)} products.")
        
        # Print summary
        print(f"\nScraping Summary:")
        print(f"Total products: {len(products)}")
        print(f"Products with datasheets: {sum(1 for p in products if p['datasheet_url'])}")
        print(f"Products with SoC info: {sum(1 for p in products if p['soc_model'])}")
        print(f"Products with memory info: {sum(1 for p in products if p['memory'])}")
        
    except KeyboardInterrupt:
        logger.info("Scraping interrupted by user")
    except Exception as e:
        logger.error(f"Scraping failed: {e}")

if __name__ == "__main__":
    main()