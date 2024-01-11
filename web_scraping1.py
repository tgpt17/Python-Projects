"""
Program: web_scraping1.py
Author: Travis Wagner
Creation Date: 4/24/2022
Description: Opens text document from the web and writes it to a new file
"""


import requests

find_text = requests.get('https://www.gutenberg.org/cache/epub/67915/pg67915.txt')
find_text.raise_for_status()
playfile = open('sun.txt', 'wb') # connect using 'wb' mode
for chunk in find_text.iter_content(100000): # method returns "chunk" of data
    playfile.write(chunk) # method writes the chunk to the file
playfile.close()