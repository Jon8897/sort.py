# Imports libaries that will be needed to run the program
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Define a function to scrape data from a list of URLs specified in a CSV file
def find_sku(filename):
    # Open the input CSV file to read from and an output CSV file to write to
    with open(filename, 'r', encoding='utf-8') as input_file, open('output.csv', 'a', newline='', encoding='utf-8') as output_file:
        # Create a CSV reader to iterate over input rows and a CSV writer for output
        reader = csv.reader(input_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        # Skip the header row in the input CSV file
        next(reader)
        # Iterate over each row in the input CSV file, with line numbers starting from 1
        for line_number, (url, description) in enumerate(reader, start=1):
            # Output the current line number to the console
            print(f'Processing line {line_number}')
            try:
                # Open the URL and retrieve its HTML content
                page = urlopen(url)
                html_bytes = page.read()
                html = html_bytes.decode('utf-8')
                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(html, 'html.parser')
                # Find the HTML element containing the SKU number using its class name and item property
                sku = soup.find('div', class_='value', itemprop="sku").string

                # If an SKU is found, write it along with the URL and description to the output CSV file
                if sku:
                    writer.writerow([sku, url, description])
                else:
                    # If no SKU is found, print a message indicating this for the current URL
                    print(f"No SKU found for URL: {url}")
            except Exception as e:
                # If an error occurs during processing, print an error message with the URL
                print(f'Error processing {url}: {e}')

# The following block will execute when the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Set the name of the input CSV file
    filename = 'input.csv'  
    # Call the scraper function with the input file name
    run_scrapper(filename)