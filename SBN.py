import re

text = ISBN 123-4-123-12345-1
# regular expression
isbn_regex = r'ISBN \d{3}-\d-\d{3}-\d{5}-\d'
#extracting data
isbn_numbers = re.findall(isbn_regex, text)
#print extracted data 
print("ISBN Numbers:", isbn_numbers)
