"""Autograder: Ch13 - Extracting Data from JSON.

Author: Virosh
"""
import urllib.request
import urllib.parse
import urllib.error
import json

# Storage, parameter, url variables
all_counts = list()
tag_counts = 0
param = dict()
param['comments'] = 'comments'
url = input('Enter URL: ')

# Urllib Functions
parse = url + urllib.parse.urlencode(param)  # parse opened url with param
print('Retrieving:', url)
url_request = urllib.request.urlopen(parse)

data = url_request.read().decode()
print('Retrieved', len(data), 'Characters')

# JSON Functions
info = json.loads(data)

for i in info['comments']:
    nums = i['count']
    all_counts.append(int(nums))
    tag_counts = tag_counts + 1

# Print final results
print('Total Tags:', tag_counts)
print('Sum:', sum(all_counts))
