 #!/usr/bin/env python3
"""
Simple test script for Axis scraper
Tests basic functionality with limited scope
"""

import sys
sys.path.append('.')

from axis_scraper import AxisScraper
import json

def test_basic_functionality():
    """Test basic scraping functionality"""
    print("Testing Axis scraper basic functionality...")
    
    scraper = AxisScraper()
    
    # Test getting main categories
    print("1. Testing category extraction...")
    categories = scraper.get_main_categories()
    print(f"Found {len(categories)} categories:")
    for i, cat in enumerate(categories[:3]):  # Show first 3
        print(f"  {i+1}. {cat['name']}")
    
    if not categories:
        print("❌ No categories found!")
        return False
    
    # Test getting collections for Network Cameras
    network_cameras = None
    for cat in categories:
        if "Network cameras" in cat['name']:
            network_cameras = cat
            break
    
    if not network_cameras:
        print("❌ Network cameras category not found!")
        return False
    
    print(f"\n2. Testing collections in '{network_cameras['name']}'...")
    collections = scraper.get_collections_in_category(
        network_cameras['url'], 
        network_cameras['name']
    )
    print(f"Found {len(collections)} collections:")
    for i, coll in enumerate(collections[:3]):  # Show first 3
        print(f"  {i+1}. {coll['name']}")
    
    if not collections:
        print("❌ No collections found!")
        return False
    
    # Test getting series for Dome Cameras
    dome_cameras = None
    for coll in collections:
        if "Dome cameras" in coll['name']:
            dome_cameras = coll
            break
    
    if not dome_cameras:
        print("❌ Dome cameras collection not found!")
        return False
    
    print(f"\n3. Testing series in '{dome_cameras['name']}'...")
    series_list = scraper.get_series_in_collection(
        dome_cameras['url'],
        dome_cameras['name'],
        dome_cameras['category']
    )
    print(f"Found {len(series_list)} series:")
    for i, series in enumerate(series_list[:3]):  # Show first 3
        print(f"  {i+1}. {series['name']}")
    
    if not series_list:
        print("❌ No series found!")
        return False
    
    # Test getting products for first series
    first_series = series_list[0]
    print(f"\n4. Testing products in '{first_series['name']}'...")
    products = scraper.get_products_in_series(
        first_series['url'],
        first_series['name'],
        first_series['collection'],
        first_series['category']
    )
    print(f"Found {len(products)} products:")
    for i, prod in enumerate(products[:2]):  # Show first 2
        print(f"  {i+1}. {prod.product_name}")
    
    if not products:
        print("❌ No products found!")
        return False
    
    # Test getting datasheet for first product
    first_product = products[0]
    print(f"\n5. Testing datasheet extraction for '{first_product.product_name}'...")
    datasheet_url = scraper.get_datasheet_url(first_product)
    if datasheet_url:
        print(f"✅ Found datasheet: {datasheet_url}")
        first_product.datasheet_url = datasheet_url
        
        # Test PDF parsing
        print("6. Testing PDF parsing...")
        pdf_info = scraper.download_and_parse_pdf(datasheet_url, first_product.product_name)
        print(f"SoC Model: {pdf_info.get('soc_model', 'Not found')}")
        print(f"Memory: {pdf_info.get('memory', 'Not found')}")
        
        # Create final result
        result = {
            "product": first_product.product_name,
            "product_url": first_product.product_url,
            "datasheet_url": datasheet_url,
            "soc_model": pdf_info.get('soc_model', ''),
            "memory": pdf_info.get('memory', ''),
            "category": first_product.category,
            "collection": first_product.collection,
            "series": first_product.series
        }
        
        # Save test result
        with open('test_result.json', 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"\n✅ Test completed successfully!")
        print(f"Result saved to test_result.json")
        return True
    else:
        print(f"❌ No datasheet found for {first_product.product_name}")
        return False

if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)