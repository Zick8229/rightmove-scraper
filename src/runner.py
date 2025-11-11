thonimport json
import os
from extractors.rightmove_parser import parse_rightmove
from outputs.exporters import export_data
from config.settings import SETTINGS

def main():
    """
    Main function to initiate the scraper and process the data.
    """
    # Load configuration
    config = SETTINGS

    # Example input URL
    input_urls = config['startUrls']

    # Extract data from URLs
    extracted_data = []
    for url in input_urls:
        data = parse_rightmove(url)
        extracted_data.append(data)

    # Export data to file
    export_data(extracted_data)

if __name__ == "__main__":
    main()