blob audio breaks downloadAudio()
1. Yeah okay so apparently the audio comes in blob, which disables any typical HTTP requests to just fetch the audio file
  1.1. I wanna look deeper into blobs, maybe later, as it's fascinating
2. GPT-kun suggested 3 workarounds, 1 is by checking if the real audio file src can be accessed in the network, 2 is by doing Selenium and JavaScript to extract blob content, and 3 is to manually download it, which is very doable
  2.1. workaround 1 doesn't work as the file is still showing to be a blob, and workaround 3 defeats the whole purpose of making this thing automated, so workaround 2 it is