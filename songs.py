import re

text =  "[Verse 1] I love you..."

#Regular Expression
song_lyrics_regex = r'\[(\w+ \d+)\]\s(.*?)\.\.\.'

#Extracting Data
song_lyrics = re.findall(song_lyrics_regex, text)

# Printing extracted data
print("Song Lyrics:", song_lyrics)
