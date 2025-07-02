 # Axis Communications Product Scraper

A Python web scraper that crawls the Axis Communications website to extract product documentation and technical specifications (SoC model and memory) from product datasheets.

## Features

- **Hierarchical crawling**: Follows the Axis website structure (Categories → Collections → Series → Products)
- **PDF parsing**: Downloads and extracts technical specifications from product datasheets
- **Robust error handling**: Includes retry logic and rate limiting
- **Progress tracking**: Saves progress periodically during long scraping sessions
- **Structured output**: Returns data in JSON format for easy processing

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

- `requests` - HTTP library for making web requests
- `beautifulsoup4` - HTML parsing library
- `PyMuPDF` - PDF processing library for extracting text
- `lxml` - Fast XML and HTML parser

## Usage

### Quick Test

To test the basic functionality on a limited set of products:

```bash
python test_scraper.py
```

This will:
1. Extract main categories from the Axis products page
2. Navigate to Network Cameras → Dome Cameras
3. Extract one product series and test PDF parsing
4. Save a test result to `test_result.json`

### Full Scraping

To run the complete scraper:

```bash
python axis_scraper.py
```

This will scrape all products following the hierarchy:
- All product categories
- All collections within each category  
- All series within each collection
- All individual products within each series

**Note**: A full scrape can take several hours due to the large number of products and rate limiting.

### Customization

You can modify the scraper behavior by editing the main function in `axis_scraper.py`:

```python
# Limit to specific categories/collections for testing
products = scraper.scrape_all_products(
    limit_categories=1,  # Only first category
    limit_collections=2  # Only first 2 collections per category
)
```

## Output Format

The scraper generates JSON output with the following structure:

```json
{
  "product": "AXIS M1055-L Box Camera",
  "product_url": "https://www.axis.com/en-us/products/axis-m1055-l",
  "datasheet_url": "https://www.axis.com/dam/public/.../datasheet-axis-m1055-l-box-camera-en-US-487307.pdf",
  "soc_model": "ARTPEC-8",
  "memory": "2 GB RAM",
  "category": "Network cameras",
  "collection": "Box cameras", 
  "series": "AXIS M10 Series"
}
```

## Website Structure

The scraper follows this hierarchy:

1. **Main Products Page**: `https://www.axis.com/en-us/products`
   - Contains product categories (Network cameras, Access control, etc.)

2. **Category Pages**: e.g., `https://www.axis.com/en-us/products/network-cameras`
   - Contains collections within the category (Dome cameras, Box cameras, etc.)

3. **Collection Pages**: e.g., `https://www.axis.com/en-us/products/dome-cameras`
   - Contains product series (AXIS M30 Series, AXIS P32 Series, etc.)

4. **Series Pages**: e.g., `https://www.axis.com/en-us/products/axis-m30-series`
   - Contains individual products or single products

5. **Product Pages**: e.g., `https://www.axis.com/en-us/products/axis-m3057-plr-mk-ii`
   - Individual product pages with `/support` subpages containing datasheets

## PDF Extraction

The scraper extracts the following information from product datasheets:

- **SoC Model**: System on Chip model (e.g., "ARTPEC-8")
- **Memory**: RAM specification (e.g., "2 GB RAM")

The extraction uses regular expressions to find these specifications in the PDF text.

## Error Handling

- **Request failures**: Automatic retry with exponential backoff
- **Rate limiting**: Configurable delays between requests (1-3 seconds by default)
- **PDF parsing errors**: Graceful handling with logging
- **Progress saving**: Periodic saves every 10 products processed

## Logging

The scraper creates detailed logs in `axis_scraper.log` including:
- Request URLs and response status
- Product discovery and processing
- PDF extraction results
- Error messages and warnings

## Files Generated

- `axis_products_final.json` - Final results
- `progress_results.json` - Periodic progress saves
- `test_result.json` - Test script output
- `axis_scraper.log` - Detailed log file
- `temp_*.pdf` - Temporary PDF files (automatically cleaned up)

## Limitations

- Only scrapes English (en-us) pages
- Focuses on Network Cameras category by default (can be modified)
- PDF extraction patterns may need updates if Axis changes their datasheet format
- Rate limiting may make full scrapes time-consuming

## Legal Considerations

- Respects robots.txt and implements reasonable rate limiting
- Only accesses publicly available product information
- Downloads only publicly available datasheets
- Use responsibly and in accordance with Axis Communications' terms of service

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

2. **Network timeouts**: Check your internet connection and try again. The scraper has built-in retry logic.

3. **PDF parsing failures**: Some PDFs may have different formats. Check the logs for details.

4. **Empty results**: The website structure may have changed. Check the HTML selectors in the code.

### Debug Mode

Enable detailed logging by modifying the logging level:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

To contribute improvements:

1. Test changes with the test script first
2. Update selectors if the website structure changes
3. Add new PDF extraction patterns if needed
4. Update documentation for any API changes
