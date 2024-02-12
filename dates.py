import re

text = "09-Feb-2005, 01-Jan-2000, 12-Dec-0012"

# Regular expressions
date_regex = r'\d{2}-[A-Za-z]{3}-\d{4}'

# Extracting Data
dates = re.findall(date_regex, text)

# Printing extracted data
print("Dates:", dates)
