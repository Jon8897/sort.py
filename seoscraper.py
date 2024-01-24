# Imports libaries that will be needed to run the program
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def run_seo_scraper(url_or_urls, window, progress_key):
    # Check if the input is a single URL string or a list of URLs
    if isinstance(url_or_urls, str):
        # If it's a string, put it into a list to standardize the processing
        urls = [url_or_urls]
    else:
        urls = url_or_urls

    # Initialize a list to hold the SEO data for each URL
    seo_data = []
    max_value = len(urls)

    # Loop through each URL in the list
    for i, url in enumerate(urls, start=1):
        try:
            # Open the URL and read the HTML content
            page = urlopen(url)
            html = page.read().decode('utf-8')
            # Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')

            # Find the title tag and extract its text, if not found return 'No Title'
            title = soup.find('title').string if soup.find('title') else 'No Title'
            # Find the meta description and extract its content
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            meta_desc_content = meta_desc['content'] if meta_desc else 'No Description'
            # Find the meta keywords and extract its content
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            meta_keywords_content = meta_keywords['content'] if meta_keywords else 'No Keywords'

            # Append a dictionary of the extracted data to the seo_data list
            seo_data.append({
                'url': url,
                'title': title,
                'description': meta_desc_content,
                'keywords': meta_keywords_content
            })

            # Update the progress bar after processing each URL
            if window and progress_key:
                window[progress_key].update(i, max_value)
                window.refresh()

        except Exception as e:
            # If there's an error during processing, print it and append an error record
            print(f'Error processing {url}: {e}')
            seo_data.append({
                'url': url,
                'title': 'Error',
                'description': 'Error',
                'keywords': 'Error'
            })

    # After the loop is done, send the results back to the event loop
    window.write_event_value('-THREAD DONE-', seo_data)

    # Return the list of SEO data
    return seo_data