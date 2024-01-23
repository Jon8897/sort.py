# Imports libaries that will be needed to run the program
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Function and reading through the csv
# Open html links and finds SKU number
def run_scrapper(filename):
    with open(filename, 'r', encoding='utf-8') as input_file, open('output.csv', 'a', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    next(reader)
    for line_number, (url, description) in enumerate(reader, start=1):
        print(f'line_number {line_number}')
        try:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            sku = soup.find('div', class_='value', itemprop="sku").string

            if sku:
                writer.writerow([sku, url, description])
            else:
                print(f"No SKU found for URL: {url}")
        except Exception as e:
                print(f'Error processing {url}: {e}')

# For standalone testing or execution
if __name__ == "__main__":
    filename = 'input.csv'  
    run_scrapper(filename)