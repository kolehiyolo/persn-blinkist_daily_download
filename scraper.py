import requests
from bs4 import BeautifulSoup

# * Input
# URL of the page to scrape
page_url = 'https://www.blinkist.com/en/reader/books/magic-pill-en'

def fetchPage(page_url):
  response = requests.get(page_url)
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup)
  return soup

# Book Title - .audio-player .m:col-span-2 .text-h6 (1st one)
def fetchTitle(soup): 
  # title = soup.select('.audio-player .text-h6')[0].text
  title_element = soup.select_one('[data-test-id="audio-player"]')
  print(title_element)
  title = title_element.text.strip() if title_element else 'Title not found'
  return title

# Book Author - .audio-player .m:col-span-2 .text-h6 (2nd one)
def fetchAuthor(soup):
  author_elements = soup.select('[data-test-id="audio-player"] .text-h6')
  author = author_elements[1].text.strip() if len(author_elements) > 1 else 'Author not found'
  return author

page_soup = fetchPage(page_url)
book_title = fetchTitle(page_soup)
book_author = fetchAuthor(page_soup)

print(f'Title: {book_title}')
print(f'Author: {book_author}')