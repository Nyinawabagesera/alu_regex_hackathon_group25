import re

text = "@Ghyghi"

#Regular Expression
twitter_username_regex = r'@\w+'

#Extracting Data
twitter_usernames = re.findall(twitter_username_regex, text)

#Printing Extracted Data
print("Twitter Usernames:", twitter_usernames)