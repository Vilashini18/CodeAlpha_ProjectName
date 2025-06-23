import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://quotes.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')


quotes = []
authors = []

for quote_block in soup.find_all('div', class_='quote'):
    text = quote_block.find('span', class_='text').get_text()
    author = quote_block.find('small', class_='author').get_text()
    
    quotes.append(text)
    authors.append(author)


df = pd.DataFrame({
    'Quote': quotes,
    'Author': authors
})

df.to_csv('quotes_dataset.csv', index=False)
print("✅ Scraping complete! Data saved as 'quotes_dataset.csv'")
