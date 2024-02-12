import re

text = "Fish (2200), Brain (9000), Power (3000)"

# Regular expression
movie_title_regex = r'.*\s\(\d{4}\)'

# Extracting Data
movie_titles = re.findall(movie_title_regex, text)

#Printing extracted data
print("Movie Titles:", movie_titles)
