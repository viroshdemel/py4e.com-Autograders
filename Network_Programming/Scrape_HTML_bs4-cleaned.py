#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
"""Autograder: Scraping HTML Data with BeautifulSoup.
@author: viroshdemel
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re

# File Selection
url = input('Enter Url: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.html'
else: url = 'http://py4e-data.dr-chuck.net/comments_1352652.html'

# Open url as html
html = urlopen(url).read()
s = soup(html, "html.parser")

# Get tags, find nums, append to list then print sum
tags = s('span')
nums = []

for tag in tags:
    num = re.findall('[0-9]+', tag.decode())
    for n in num: nums.append(int(n))
print(sum(nums))
