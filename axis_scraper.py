#!/usr/bin/env python3
"""
Axis Communications Product Scraper
Enhanced version with comprehensive logging, timing, and progress tracking
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
from dataclasses import dataclass, field
import random
from datetime import datetime, timedelta

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
    youtube_video_url: str = ""

@dataclass
class ScrapingStats:
    """Data class for tracking scraping statistics"""
    start_time: datetime
    categories_found: int = 0
    categories_processed: int = 0
    collections_found: int = 0
    collections_processed: int = 0
    series_found: int = 0
    series_processed: int = 0
    products_found: int = 0
    products_processed: int = 0
    products_with_datasheets: int = 0
    products_with_soc: int = 0
    products_with_memory: int = 0
    products_with_youtube_videos: int = 0
    categories_scraped: List[str] = field(default_factory=list)
    collections_scraped: List[str] = field(default_factory=list)

class AxisScraper:
    def __init__(self, base_url: str = "https://www.axis.com", delay_range: tuple = (1, 3), download_pdfs: bool = True):
        """
        Initialize the Axis Communications product scraper.
        
        Args:
            base_url (str): Base URL for Axis Communications website. Defaults to "https://www.axis.com".
            delay_range (tuple): Range for random delays between requests in seconds. Defaults to (1, 3).
            download_pdfs (bool): Whether to download and parse PDF datasheets for SoC and memory info. 
                                Defaults to True. Set to False for faster scraping when detailed specs are not needed.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.delay_range = delay_range
        self.download_pdfs = download_pdfs
        self.products = []
        self.stats = None
        
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
        logger.info(f"🔍 Fetching main categories from: {url}")
        
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
                logger.debug(f"Found category: {category_name}")
        
        if self.stats:
            self.stats.categories_found = len(categories)
        
        logger.info(f"📋 Found {len(categories)} total categories: {[cat['name'] for cat in categories]}")
        return categories
    
    def get_collections_in_category(self, category_url: str, category_name: str) -> List[Dict[str, str]]:
        """Get collections within a category"""
        logger.info(f"📂 Processing category: '{category_name}'")
        
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
                logger.debug(f"Found collection: {collection_name}")
        
        if self.stats:
            self.stats.collections_found += len(collections)
            self.stats.categories_scraped.append(category_name)
        
        logger.info(f"  📁 Found {len(collections)} collections in '{category_name}': {[coll['name'] for coll in collections]}")
        return collections
    
    def get_series_in_collection(self, collection_url: str, collection_name: str, category_name: str) -> List[Dict[str, str]]:
        """Get product series within a collection"""
        logger.info(f"  📦 Processing collection: '{collection_name}' in '{category_name}'")
        
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
                logger.debug(f"Found series: {series_name}")
        
        if self.stats:
            self.stats.series_found += len(series_list)
            collection_full_name = f"{category_name} > {collection_name}"
            if collection_full_name not in self.stats.collections_scraped:
                self.stats.collections_scraped.append(collection_full_name)
        
        logger.info(f"    📊 Found {len(series_list)} series in collection '{collection_name}': {[series['name'] for series in series_list]}")
        return series_list
    
    def get_products_in_series(self, series_url: str, series_name: str, collection_name: str, category_name: str) -> List[ProductInfo]:
        """Get individual products within a series"""
        logger.info(f"    🔍 Processing series: '{series_name}' in '{collection_name}'")
        
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
                    logger.debug(f"Found product: {product_name}")
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
                logger.debug(f"Found single product: {product_name}")
        
        if self.stats:
            self.stats.products_found += len(products)
        
        logger.info(f"      📱 Found {len(products)} products in series '{series_name}': {[p.product_name for p in products]}")
        return products
    
    def get_datasheet_url(self, product: ProductInfo) -> str:
        """Get datasheet PDF URL from product support page"""
        support_url = f"{product.product_url}/support"
        logger.debug(f"Checking for datasheet: {product.product_name}")
        
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
                        logger.debug(f"Found datasheet: {datasheet_url}")
                        return datasheet_url
        
        logger.debug(f"No datasheet found for {product.product_name}")
        return ""
    
    def get_youtube_video_url(self, product: ProductInfo) -> str:
        """Get YouTube video URL from product page"""
        logger.debug(f"🎥 Checking for YouTube video: {product.product_name}")
        
        response = self._make_request(product.product_url)
        if not response:
            return ""
        
        soup = self._parse_html(response)
        if not soup:
            return ""
        
        try:
            # Look for the specific video embed div
            video_div = soup.find('div', class_='video-embed-field-provider-youtube video-embed-field-responsive-video')
            if not video_div:
                logger.debug(f"No YouTube video div found for {product.product_name}")
                return ""
            
            # Find the iframe inside the div
            iframe = video_div.find('iframe')
            if not iframe:
                logger.debug(f"No iframe found in video div for {product.product_name}")
                return ""
            
            # Get the src attribute
            video_url = iframe.get('src')
            if video_url and 'youtube.com/embed' in video_url:
                logger.debug(f"Found YouTube video: {video_url}")
                return video_url
            
            # Also check data-src as fallback
            data_src = iframe.get('data-src')
            if data_src and 'youtube.com/embed' in data_src:
                logger.debug(f"Found YouTube video (data-src): {data_src}")
                return data_src
                
            logger.debug(f"No valid YouTube URL found for {product.product_name}")
            return ""
            
        except Exception as e:
            logger.error(f"Failed to extract YouTube video URL for {product.product_name}: {e}")
            return ""

    def download_and_parse_pdf(self, pdf_url: str, product_name: str) -> Dict[str, str]:
        """Download PDF and extract SoC model and memory information"""
        logger.debug(f"📄 Downloading and parsing PDF for: {product_name}")
        
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
            
            logger.debug(f"Extracted - SoC: {soc_model}, Memory: {memory}")
            
        except Exception as e:
            logger.error(f"Failed to extract from PDF {pdf_path}: {e}")
        
        return {"soc_model": soc_model, "memory": memory}
    
    def scrape_all_products(self, limit_categories: int = None, limit_collections: int = None) -> List[Dict]:
        """Main method to scrape all products with comprehensive logging"""
        start_time = datetime.now()
        self.stats = ScrapingStats(start_time=start_time)
        
        logger.info("🚀 Starting comprehensive Axis Communications product scrape")
        logger.info(f"⏰ Scrape started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Get main categories
        categories = self.get_main_categories()
        # if limit_categories:
        #     categories = categories[:limit_categories]
        #     logger.info(f"🔒 Limited to first {limit_categories} categories")
        
        all_products = []
        
        for cat_idx, category in enumerate(categories, 1):
            category_start_time = datetime.now()
            logger.info(f"\n{'='*80}")
            logger.info(f"📂 PROCESSING CATEGORY {cat_idx}/{len(categories)}: '{category['name']}'")
            logger.info(f"{'='*80}")
                
            # Get collections in category
            collections = self.get_collections_in_category(category['url'], category['name'])
            # if limit_collections:
            #     collections = collections[:limit_collections]
            #     logger.info(f"🔒 Limited to first {limit_collections} collections per category")
            
            self.stats.categories_processed += 1
            
            for coll_idx, collection in enumerate(collections, 1):
                collection_start_time = datetime.now()
                logger.info(f"\n{'-'*60}")
                logger.info(f"📁 PROCESSING COLLECTION {coll_idx}/{len(collections)}: '{collection['name']}'")
                logger.info(f"{'-'*60}")
                
                # Get series in collection
                series_list = self.get_series_in_collection(
                    collection['url'], 
                    collection['name'], 
                    collection['category']
                )
                
                self.stats.collections_processed += 1
                
                for series_idx, series in enumerate(series_list, 1):
                    series_start_time = datetime.now()
                    logger.info(f"\n📦 Processing series {series_idx}/{len(series_list)}: '{series['name']}'")
                    
                    # Get products in series
                    products = self.get_products_in_series(
                        series['url'],
                        series['name'],
                        series['collection'],
                        series['category']
                    )
                    
                    self.stats.series_processed += 1
                    
                    for prod_idx, product in enumerate(products, 1):
                        product_start_time = datetime.now()
                        logger.info(f"      🔍 Processing product {prod_idx}/{len(products)}: '{product.product_name}'")
                        
                        # Get datasheet URL (always try to find the URL)
                        product.datasheet_url = self.get_datasheet_url(product)
                        
                        # Get YouTube video URL
                        product.youtube_video_url = self.get_youtube_video_url(product)
                        if product.youtube_video_url:
                            self.stats.products_with_youtube_videos += 1
                            logger.info(f"        🎥 Found YouTube video for '{product.product_name}'")
                        
                        if product.datasheet_url:
                            self.stats.products_with_datasheets += 1
                            logger.info(f"        📄 Found datasheet for '{product.product_name}'")
                            
                            # Only download and parse PDF if enabled
                            if self.download_pdfs:
                                # Extract info from PDF
                                pdf_info = self.download_and_parse_pdf(
                                    product.datasheet_url, 
                                    product.product_name
                                )
                                product.soc_model = pdf_info["soc_model"]
                                product.memory = pdf_info["memory"]
                                
                                if product.soc_model:
                                    self.stats.products_with_soc += 1
                                    logger.info(f"        🔧 Extracted SoC: {product.soc_model}")
                                if product.memory:
                                    self.stats.products_with_memory += 1
                                    logger.info(f"        💾 Extracted Memory: {product.memory}")
                            else:
                                logger.info(f"        ⏭️  PDF download disabled - skipping datasheet parsing")
                        else:
                            logger.warning(f"        ❌ No datasheet found for '{product.product_name}'")
                        
                        # Convert to dict for output
                        product_dict = {
                            "product": product.product_name,
                            "product_url": product.product_url,
                            "datasheet_url": product.datasheet_url,
                            "soc_model": product.soc_model,
                            "memory": product.memory,
                            "category": product.category,
                            "collection": product.collection,
                            "series": product.series,
                            "youtube_video_url": product.youtube_video_url
                        }
                        
                        all_products.append(product_dict)
                        self.stats.products_processed += 1
                        
                        product_elapsed = datetime.now() - product_start_time
                        logger.info(f"        ✅ Completed product '{product.product_name}' in {product_elapsed.total_seconds():.1f}s")
                        
                        # Save progress periodically
                        if len(all_products) % 10 == 0:
                            self.save_results(all_products, "progress_results.json")
                            logger.info(f"💾 Progress saved: {len(all_products)} products processed")
                    
                    series_elapsed = datetime.now() - series_start_time
                    logger.info(f"✅ Completed series '{series['name']}' ({len(products)} products) in {series_elapsed.total_seconds():.1f}s")
                
                collection_elapsed = datetime.now() - collection_start_time
                logger.info(f"✅ Completed collection '{collection['name']}' ({len(series_list)} series) in {collection_elapsed.total_seconds():.1f}s")
            
            category_elapsed = datetime.now() - category_start_time
            logger.info(f"✅ Completed category '{category['name']}' ({len(collections)} collections) in {category_elapsed.total_seconds():.1f}s")
        
        # Log final statistics
        self._log_final_statistics(start_time)
        
        return all_products
    
    def _log_final_statistics(self, start_time: datetime):
        """Log comprehensive final statistics"""
        end_time = datetime.now()
        total_elapsed = end_time - start_time
        
        logger.info(f"\n{'='*80}")
        logger.info(f"🎉 SCRAPING COMPLETED!")
        logger.info(f"{'='*80}")
        logger.info(f"⏰ Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"⏰ Ended: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"⏱️  Total execution time: {total_elapsed}")
        logger.info(f"📊 FINAL STATISTICS:")
        logger.info(f"   📋 Categories found: {self.stats.categories_found}")
        logger.info(f"   📂 Categories processed: {self.stats.categories_processed}")
        logger.info(f"   📁 Collections found: {self.stats.collections_found}")
        logger.info(f"   📦 Collections processed: {self.stats.collections_processed}")
        logger.info(f"   📊 Series found: {self.stats.series_found}")
        logger.info(f"   🔧 Series processed: {self.stats.series_processed}")
        logger.info(f"   📱 Products found: {self.stats.products_found}")
        logger.info(f"   ✅ Products processed: {self.stats.products_processed}")
        logger.info(f"   📄 Products with datasheets: {self.stats.products_with_datasheets}")
        logger.info(f"   🔧 Products with SoC info: {self.stats.products_with_soc}")
        logger.info(f"   💾 Products with memory info: {self.stats.products_with_memory}")
        logger.info(f"📂 Categories scraped: {self.stats.categories_scraped}")
        logger.info(f"📁 Collections scraped:")
        for collection in self.stats.collections_scraped:
            logger.info(f"   - {collection}")
    
    def save_results(self, products: List[Dict], filename: str = "axis_products.json"):
        """Save results to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(products, f, indent=2, ensure_ascii=False)
            logger.debug(f"Saved {len(products)} products to {filename}")
        except Exception as e:
            logger.error(f"Failed to save results: {e}")

def main():
    """Main execution function with enhanced logging and timing"""
    # Initialize scraper with PDF downloading enabled (default)
    # To disable PDF downloading for faster scraping, use: AxisScraper(download_pdfs=False)
    scraper = AxisScraper(download_pdfs=False)
    
    logger.info("🚀 Starting enhanced Axis Communications product scraper")
    logger.info(f"📄 PDF downloading: {'✅ Enabled' if scraper.download_pdfs else '❌ Disabled'}")
    
    try:
        # Scrape products (limit for testing)
        products = scraper.scrape_all_products(limit_categories=12, limit_collections=2)
        
        # Save final results
        scraper.save_results(products, "axis_products_final.json")
        
        logger.info(f"🎉 Scraping completed successfully!")
        logger.info(f"📊 Final results: {len(products)} products saved to axis_products_final.json")
        
        # Print summary to console
        if scraper.stats:
            print(f"\n{'='*60}")
            print(f"🎉 SCRAPING SUMMARY")
            print(f"{'='*60}")
            print(f"📄 PDF downloading: {'✅ Enabled' if scraper.download_pdfs else '❌ Disabled'}")
            print(f"⏱️  Total execution time: {datetime.now() - scraper.stats.start_time}")
            print(f"📋 Categories processed: {scraper.stats.categories_processed}/{scraper.stats.categories_found}")
            print(f"📁 Collections processed: {scraper.stats.collections_processed}")
            print(f"📦 Series processed: {scraper.stats.series_processed}")
            print(f"📱 Products processed: {scraper.stats.products_processed}")
            print(f"📄 Products with datasheets: {scraper.stats.products_with_datasheets}")
            print(f"🔧 Products with SoC info: {scraper.stats.products_with_soc}")
            print(f"💾 Products with memory info: {scraper.stats.products_with_memory}")
            print(f"🎥 Products with YouTube videos: {scraper.stats.products_with_youtube_videos}")
            print(f"📂 Categories: {', '.join(scraper.stats.categories_scraped)}")
            print(f"📁 Collections: {', '.join(scraper.stats.collections_scraped)}")
            print(f"{'='*60}")
        
    except KeyboardInterrupt:
        logger.info("⏹️  Scraping interrupted by user")
        if scraper.products:
            scraper.save_results(scraper.products, "interrupted_results.json")
            logger.info(f"💾 Partial results saved: {len(scraper.products)} products")
    except Exception as e:
        logger.error(f"❌ Scraping failed: {e}")
        if scraper.products:
            scraper.save_results(scraper.products, "error_results.json")
            logger.info(f"💾 Partial results saved: {len(scraper.products)} products")

if __name__ == "__main__":
    main() 