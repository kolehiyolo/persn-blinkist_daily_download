Selenium failing
1. Wow so after some fenagling, the page is being opened but it ain't loading
2. I checked the console and apparently some 403s are being thrown by the server hahahaha
3. That surely means that they're refusing the request, possibly due to the bot nature
4. As a very very very bad and temporary workaround, I decided to just make it so that I will be manually downloading/copying the live page HTML, pasting it to some input file, then I have the scraper fetching the text content and the audio src from that
  4.1. Very very bad UX but I need at least a working version today, just to feel good lol
5. The next option is to make this thing into a Chrome extension instead, as surely that will have access to the live page HTML without raising any flags