import re

text = "#ffffff"

#Regular Expression
hex_colors = re.findall(r'#([A-Fa-f0-9]{6})')

#Extracting Data
if len(hex_colors.findall(text)) != 0:
    print(f"Matches: {color_pattern.findall(text)}")
else:
    print(f"{text} has no matches")
