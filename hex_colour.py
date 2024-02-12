import re

text = "#ffffff, #FF001, #FF0000"

#Regular Expression
hex_color_regex = r'#([A-Fa-f0-9]{6})'

#Extracting Data
hex_colors = re.findall(hex_color_regex, text)

#Printing Extracted Data
print("Hex Color Codes:", hex_colors)
