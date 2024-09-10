from datetime import datetime
import os
from bs4 import BeautifulSoup

# * Input
# kPath to the HTML file
html_file_path = 'input/page.html'

# folder path to save the output
default_root_folder_path = 'output'

# * FUNCTIONS
# Create a folder with the given name in the default root folder path
# Input: Default root folder path, string; Folder name, string
# Output: A folder created in the default root folder, void; Folder path, string
def createFolder(default_root_folder_path, folder_name):
  try:
    folder_path = f'{default_root_folder_path}/{folder_name}'
    os.makedirs(folder_path)
    return folder_path
  except FileExistsError:
    pass
  
# Create a folder name using the timestamp, book title, and book author
# Input: Timestamp, string; Book title, string; Book author, string
# Output: Folder name, string
def createFolderName(timestamp, book_title, book_author):
  folder_name = f'{timestamp} - {book_author} - {book_title}'
  return folder_name

# Create a timestamp in the format 'YYYY-MM-DD-NN'
# Input: default_root_folder_path, string
# Output: Timestamp, string
# NN represents the count of folders existing for that timestamp, so for example, if there's already 2024-09-10-01 and teh timestamp is 2024-09-10, the new timestamp should then be 2024-09-10-02
# This NN should come in handy if it gets to the point that you can do multiple scrapes per day
def createTimeStamp(default_root_folder_path):
  # Get the YYYY-MM-DD timestamp first
  timestamp = datetime.now().strftime('%Y-%m-%d')
  
  # Check if folders starting with the timestamp already exist in the default root folder path
  match_count = countMatchingTimeStamps(default_root_folder_path, timestamp)
  
  # Append the count to the timestamp, adding 1 to the count
  timestamp = f'{timestamp}-{str(match_count + 1).zfill(2)}'
      
  return timestamp

# Check if the timestamp already has folders in the default root folder path
# Input: default_root_folder_path, string, Timestamp, string
# Output: number of folders matching the timestamp, int
def countMatchingTimeStamps(default_root_folder_path, timestamp):
  # Check if folders starting with the timestamp already exist in the default root folder path
  matching_folders = [folder for folder in os.listdir(default_root_folder_path) if folder.startswith(timestamp)]
  
  # Get the count
  match_count = len(matching_folders)
  
  return match_count
  
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
def main(html_file_path, default_root_folder_path):
  # Fetch the page
  page_soup = fetchPageFromFile(html_file_path)

  # Get the title, author, and audio src
  book_title = fetchTitle(page_soup)
  book_author = fetchAuthor(page_soup)
  # audio_src = fetchAudioSrc(page_soup)
  
  # Creating the folder
  timestamp = createTimeStamp(default_root_folder_path)
  folder_name = createFolderName(timestamp, book_title, book_author)
  createFolder(default_root_folder_path, folder_name)

  # Output the title, author, and audio src
  print(f'Title: {book_title}')
  print(f'Author: {book_author}')
  # print(f'Audio Source: {audio_src}')
  
# * Run the main function
main(html_file_path, default_root_folder_path)