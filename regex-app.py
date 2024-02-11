import re

text = "Fish (2002), 01-10-2000, ISBN 123-4-123-12345-1, 192.098.190.075"


#Regular Expression
movie_title_regex = r'.*\s\(\d{4}\)'
date_regex = r'\d{2}-[A-Za-z]{3}-\d{4}'
isbn_regex = r'ISBN \d{3}-\d-\d{3}-\d{5}-\d'
ip_address_regex = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}'

#Extracting Data
movie_titles = re.findall(movie_title_regex, text)
dates = re.findall(date_regex, text)
isbn_numbers = re.findall(isbn_regex, text)
ip_addresses = re.findall(ip_address_regex, text)

#Printing Extracted Data
print("Movie Titles:", movie_titles)
print("Dates:", dates)
print("ISBN Numbers:", isbn_numbers)
print("IP Addresses:", ip_addresses)