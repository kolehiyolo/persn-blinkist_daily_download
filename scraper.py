from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Selenium WebDriver (e.g., for Chrome)
chromedriver_path = "./selenium/chromedriver-win64/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Use incognito mode
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Set a custom User-Agent to mimic a real browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options.add_argument(f'user-agent={user_agent}')

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    """
})

# Input: URL of the page to scrape
page_url = 'https://www.blinkist.com/en/reader/books/magic-pill-en'
pageCloseDelay = 30  # Delay in seconds before closing the page

# Fetch the page content with Selenium
def fetchPage(page_url):
    driver.get(page_url)
    print("Page loaded")
    return driver

# Fetch book title using 'data-test-id' attribute for 'audio-player'
def fetchTitle(driver):
    try:
        # Wait for the title element to load before scraping
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="audio-player"] .text-h6'))
        )
        title_element = driver.find_element(By.CSS_SELECTOR, '[data-test-id="audio-player"] .text-h6')
        title = title_element.text.strip()
    except Exception as e:
        title = 'Title not found'
        print(f'Error fetching title: {e}')
    return title

# Fetch book author using 'data-test-id' attribute for 'audio-player'
def fetchAuthor(driver):
    try:
        # Wait for author elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test-id="audio-player"] .text-h6'))
        )
        author_elements = driver.find_elements(By.CSS_SELECTOR, '[data-test-id="audio-player"] .text-h6')
        author = author_elements[1].text.strip() if len(author_elements) > 1 else 'Author not found'
    except Exception as e:
        author = 'Author not found'
        print(f'Error fetching author: {e}')
    return author

# Fetch the page
page_driver = fetchPage(page_url)

# Get the title and author
book_title = fetchTitle(page_driver)
book_author = fetchAuthor(page_driver)

# Output the title and author
print(f'Title: {book_title}')
print(f'Author: {book_author}')

# Wait for the specified time before closing the browser
print(f'Waiting for {pageCloseDelay} seconds before closing the page...')
time.sleep(pageCloseDelay)

# Close the Selenium WebDriver session
driver.quit()
