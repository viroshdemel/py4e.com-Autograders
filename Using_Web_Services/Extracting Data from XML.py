"""Autograder Ch13: Extracting Data from XML.

[ROUGH DRAFT]
Author: Virosh De Mel
Start Date: 17-01-2022
"""
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
# import re

all_counts = list()
params = dict()
params['comment'] = 'comment'
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
parse = url + urllib.parse.urlencode(params)
url_request = urllib.request.urlopen(url)

data = url_request.read()  # Taking URL page content and reading byte data

# print(data)  # XML data
# print(type(data))  # XML bytes
print('Retrieved', len(data), 'Characters')

# print(data.decode())
# print(type(data.decode()))  # class 'str'

tree = ET.fromstring(data)  # From data variable use ET function to parse xml

counts = tree.findall('.//count')  # From tree root elements, finding tag count
# print(counts)

# print(counts.tostring())

for c in counts:
    # num = dict()
    # print(c.text)
    all_counts.append(int(c.text))
    # s = ET.tostring(c).decode()
    # print(type(s))  # class str
    # print(s)
    # numers = re.findall('.([0-9]+)', s)
    # for n in numers:
    #    all_counts.append(int(n))
    # print(numers)
    # all_counts.append(numers)
    # print(all_counts)

print('Sum:', sum(all_counts))
