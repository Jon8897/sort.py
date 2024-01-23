# Imports libaries that will be needed to run the program
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def run_seo_scraper(url_or_urls):
    # If the input is a single URL string, convert it to a list with one URL
    if isinstance(url_or_urls, str):
        urls = [url_or_urls]
    else:
        urls = url_or_urls

    seo_data = []

    for url in urls:
        try:
            page = urlopen(url)
            html = page.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')

            title = soup.find('title').string if soup.find('title') else 'No Title'
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            meta_desc_content = meta_desc['content'] if meta_desc else 'No Description'
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            meta_keywords_content = meta_keywords['content'] if meta_keywords else 'No Keywords'

            seo_data.append({
                'url': url,
                'title': title,
                'description': meta_desc_content,
                'keywords': meta_keywords_content
            })
        except Exception as e:
            print(f'Error processing {url}: {e}')
            seo_data.append({
                'url': url,
                'title': 'Error',
                'description': 'Error',
                'keywords': 'Error'
            })

    return seo_data

# Example usage for a single URL:
# result = run_seo_scraper('http://example.com')
# print(result)

# Example usage for multiple URLs:
# urls = ['http://example.com', 'http://example.org']
# results = run_seo_scraper(urls)
# print(results)