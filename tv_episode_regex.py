import re

text = "Fish S01E02:Little Rat"

#Regular Expression
tv_episode_regex = r'.* S\d{2}E\d{2}: .*'

#Extracting Data
tv_episode_titles = re.findall(tv_episode_regex, text)

#Printing Extracted Data
print("TV Episode Titles:", tv_episode_titles)
