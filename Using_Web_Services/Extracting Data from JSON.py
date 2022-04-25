"""Autograder: Ch13 - Extracting Data from JSON.

Author: Virosh
Start Date: 21-01-2022
"""
import urllib.request
import urllib.parse
import urllib.error
import json

# Storage and Retrieval Variables
all_counts = list()
param = dict()
param['comments'] = 'comments'
# print(param)
url = 'http://py4e-data.dr-chuck.net/comments_42.json'

# Urllib Functions
parse = url + urllib.parse.urlencode(param)  # parse opened url with param
# print(parse)
print('Retrieving:', url)
url_request = urllib.request.urlopen(parse)
# print(url_request)

data = url_request.read().decode()
print('Retrieved', len(data), 'Characters')
# print(data)

# JSON Functions
info = json.loads(data)
# print(info)

for i in info['comments']:
    nums = i['count']
    all_counts.append(int(nums))

print(sum(all_counts))
