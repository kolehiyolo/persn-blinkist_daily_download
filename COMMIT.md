Create timestamp, folder name, and new folder
1. YOOO alright so the new folder is now being created, with the folder name being determined by a timestamp and the book title and author
2. Created dedicated functions for the various input-output processed needed to make this work
3. The timestamp isn't perfect, though, as it's now YYYY-MM-DD when it should be YYYY-MM-DD-NN, with NN representing the count of folders existing for that timestamp, so for example, if there's already 2024-09-10-01 and teh timestamp is 2024-09-10, the new timestamp should then be 2024-09-10-02
  3.1. This NN should come in handy if it gets to the point that you can do multiple scrapes per day