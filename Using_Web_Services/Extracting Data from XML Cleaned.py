"""Autograder Ch13: Extracting Data from XML.

Author: Virosh
"""
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# Necessary storage and retrieval Variables
all_counts = list()
Count = 0
params = dict()
params['comment'] = 'comment'  # Urllib parameter for XML tag
url = input('Enter a URL: ')

# Urllib Functions
parse = url + urllib.parse.urlencode(params)
url_request = urllib.request.urlopen(url)
print('Retrieving:', url)

# ElementTree Process
data = url_request.read()  # Taking URL page content and reading byte data
print('Retrieved', len(data), 'Characters')

tree = ET.fromstring(data)  # From data variable use ET function to parse xml

counts = tree.findall('.//count')  # From tree root elements, finding tag count

# Loop through counts and save numbers in list format
for c in counts:
    all_counts.append(int(c.text))
    Count = Count + 1

# Print total count tags and Sum of all numbers in count
print('Count:', Count)
print('Sum:', sum(all_counts))
