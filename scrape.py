from bs4 import BeautifulSoup
import requests
from collections import Counter
import re

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        words = re.findall(r'\b\w+\b', text.lower())

        word_frequency = dict(Counter(words))


        return {
            'url': url,
            'content': text,
            'word_frequency': word_frequency
        }
    
    except requests.RequestException as e:
        print(f"An error occurred while trying to scrape the website: {e}")
        return None