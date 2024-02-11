import re

text = "Fish (2002), 01-10-2000"

#Regular Expression
movie_title_regex = r'.*\s\(\d{4}\)'
date_regex = r'\d{2}-[A-Za-z]{3}-\d{4}'

#Extracting Data
movie_titles = re.findall(movie_title_regex, text)
dates = re.findall(date_regex, text)

#Printing Extracted Data
print("Movie Titles:", movie_titles)
print("Dates:", dates)
