# imports libaries that will be needed to run the program
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#function and reading through the csv
#open html links and finds SKU number
def run_scrapper(filename):
    input_file = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(input_file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    output_file = open('output.csv', 'a', newline='')
    writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    next(reader)
    line_number = 0
    for url, description in reader:
        line_number = line_number + 1
        print(line_number)
        try:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            sku = soup.find('div', class_='value', itemprop="sku").string

            writer.writerow([sku, url, description])
        except Exception as e:
            print(f'Error processing {url}: {e}')
            continue