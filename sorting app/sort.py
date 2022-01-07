#links tools need to create running software
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

#reads the file created
filename = 'pyhtontestdata.csv'
input_file = open('pythontestdata.csv', 'r', encoding= 'utf-8')
reader = csv.reader(input_file, delimiter=',', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)

#creates an output file for a csv document
output_file = open('output.csv', 'a', newline='')
writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

#used to read the url and find the sku number
#to convert url to sku product number
#Shows progress through line number
header = next(reader)
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

    except:
        print('sku not found')
        continue