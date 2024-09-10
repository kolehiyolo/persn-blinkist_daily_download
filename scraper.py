from bs4 import BeautifulSoup

# * Input
# kPath to the HTML file
html_file_path = 'input/page.html'

# * FUNCTIONS
# Fetch the page content from the local HTML file
# Input: HTML file path, string
# Output: BeautifulSoup object containing the parsed HTML content
def fetchPageFromFile(html_file_path):
  with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
  soup = BeautifulSoup(html_content, 'html.parser')
  return soup

# Fetch book title using 'data-test-id' attribute for 'audio-player'
# Input: BeautifulSoup object containing the parsed HTML content
# Output: Title of the book, string
# The title and author HTML are contained in .text-h6 elements within the audio-player element, the title being the first and the author being the second
# If the title is not found, return 'Title not found', although this should not happen unless the page is broken or the HTML structure has changed
def fetchTitle(soup):
  try:
    title_element = soup.select_one('[data-test-id="audio-player"] .text-h6')
    title = title_element.text.strip() if title_element else 'Title not found'
  except Exception as e:
    title = 'Title not found'
    print(f'Error fetching title: {e}')
  return title

# Fetch book author using 'data-test-id' attribute for 'audio-player'
# Input: BeautifulSoup object containing the parsed HTML content
# Output: Author of the book, string
# If the author is not found, return 'Author not found', although this should not happen unless the page is broken or the HTML structure has changed
def fetchAuthor(soup):
  try:
    author_elements = soup.select('[data-test-id="audio-player"] .text-h6')
    author = author_elements[1].text.strip() if len(author_elements) > 1 else 'Author not found'
  except Exception as e:
    author = 'Author not found'
    print(f'Error fetching author: {e}')
  return author

# ! Review later
# Fetch audio src using 'data-test-id' attribute for 'audio-player'
def fetchAudioSrc(soup):
  try:
    audio_element = soup.select_one('[data-test-id="audio-player"] audio')
    audio_src = audio_element['src'] if audio_element else 'Audio source not found'
  except Exception as e:
    audio_src = 'Audio source not found'
    print(f'Error fetching audio source: {e}')
  return audio_src

# * MAIN FUNCTION
def main(html_file_path):
  # Fetch the page
  page_soup = fetchPageFromFile(html_file_path)

  # Get the title, author, and audio src
  book_title = fetchTitle(page_soup)
  book_author = fetchAuthor(page_soup)
  # audio_src = fetchAudioSrc(page_soup)

  # Output the title, author, and audio src
  print(f'Title: {book_title}')
  print(f'Author: {book_author}')
  # print(f'Audio Source: {audio_src}')
  
# * Run the main function
main(html_file_path)