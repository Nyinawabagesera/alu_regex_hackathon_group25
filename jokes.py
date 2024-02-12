import re

text = "Why did the car run ? Because nothing"

#Regular Expression
jokes_regex = r'Why did the .*? Because.*\,'

#Extracting Data
jokes = re.findall(jokes_regex, text)

#Printing Extracted Data
print("Jokes:", jokes)