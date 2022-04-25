#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Autograder: Ch13 - Using GeoJSON API.

@author: virosh
"""
import urllib.request
import urllib.parse
import urllib.error
import json

# Address, api key, parameter, url variables
address = input('Enter Address: ')
api_key = 42
param = dict()
param['address'] = address
param['key'] = api_key
url = 'https://py4e-data.dr-chuck.net/json?'

# Urllib Functions
parse = url + urllib.parse.urlencode(param)
print('Retrieve:', parse)
request = urllib.request.urlopen(parse)

data = request.read().decode()
print('Retrieved', len(data), 'Characters')

# JSON Functions
info = json.loads(data)
# print(json.dumps(info, indent=4))  # prints in prettier format
print('place_id:', info['results'][0]['place_id'])

