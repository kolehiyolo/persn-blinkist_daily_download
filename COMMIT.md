Fetch text content
1. Alrightalright so the text content from the HTML has been extracted
2. First step was to get the chapter elements onto a list chapters_html
3. Then, run a loop through chapters_html, calling fetchContentFromChapter(),which accepts chapter_html as input, then outputs a dictionary with subtitle, title, and content properties
4. To test, I have a loop printing the subtitle and title per chapter