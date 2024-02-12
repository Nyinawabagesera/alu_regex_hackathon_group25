import re

text = "192.098.190.075"



#regular expression
ip_address_regex =  r'\b((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' \
                   r'\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' \
                   r'\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' \
                   r'\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b'

#Extracting Data
ip_addresses = re.findall(ip_address_regex, text)

#Printing Extracted Data

print("IP Addresses:", ip_addresses)
