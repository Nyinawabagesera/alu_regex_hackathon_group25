import re

text = "Fish (2002), 01-Mar-2000, ISBN 123-4-123-12345-1, 192.098.190.075, #ffffff, Fish S01E02:Little Rat, @Ghyghi, [Verse 1] I love you..., Why did the car run ? Because nothing"


#Regular Expression
movie_title_regex = r'.*\s\(\d{4}\)'
date_regex = r'\d{2}-[A-Za-z]{3}-\d{4}'
isbn_regex = r'ISBN \d{3}-\d-\d{3}-\d{5}-\d'
ip_address_regex = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}'
hex_color_regex = r'#([A-Fa-f0-9]{6})'
tv_episode_regex = r'.* S\d{2}E\d{2}: .*'
song_lyrics_regex = r'\[(\w+ \d+)\]\s(.*?)\.\.\.'
twitter_username_regex = r'@\w+'
jokes_regex = r'Why did the .*? Because.*\,'

#Extracting Data
movie_titles = re.findall(movie_title_regex, text)
dates = re.findall(date_regex, text)
isbn_numbers = re.findall(isbn_regex, text)
ip_addresses = re.findall(ip_address_regex, text)
hex_colors = re.findall(hex_color_regex, text)
tv_episode_titles = re.findall(tv_episode_regex, text)
song_lyrics = re.findall(song_lyrics_regex, text)
twitter_usernames = re.findall(twitter_username_regex, text)
jokes = re.findall(jokes_regex, text)

matches = re.findall(song_lyrics_regex, text)
lyrics_array = [(section, lyrics + '...,') for section, lyrics in matches]

#Printing Extracted Data
print("Movie Titles:", movie_titles)
print("Dates:", dates)
print("ISBN Numbers:", isbn_numbers)
print("IP Addresses:", ip_addresses)
print("Hex Color Codes:", hex_colors)
print("TV Episode Titles:", tv_episode_titles)
print("Song Lyrics:", lyrics_array)
print("Twitter Usernames:", twitter_usernames)
print("Jokes:", jokes)

