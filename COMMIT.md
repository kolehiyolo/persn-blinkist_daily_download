Failed using Selenium+JavaScript to extract blob audio
1. Okay so it isn't working, and that's because Selenium creates a sort of incognito instance of chrome, and the blob link doesn't load on incognito
2. The only way forward that I can see is to make the whole thing into a Chrome extension, as I assume that will have direct access to already active and valid page on the browser, instead of a Selenium-lead instance that can be detected as bot activity
3. A= a workaround, scraper.py can at least scrape the HTML contents already into a MD, but the audio download has to be done manually for now