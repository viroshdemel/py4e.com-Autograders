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
#print(file)

# Open url as html
html = urlopen(url).read()
#print(html)
s = soup(html, "html.parser")
#print(s)  #prints span tags
#print(type(s))  #<class 'bs4.BeautifulSoup'>

# Collect tags
tags = s('span')
#print(tags)

nums = []
for tag in tags:
    #print(type(tag))
    #print(tag.re.compile(r'9'))  #Nonetype obj has no attr compile
    #print(re.findall('[0-9]+', tag))  #Expected str or bytes-like obj
    #print(type(tag.decode()))  #str
    #print(re.findall('[0-9]+', tag.decode()))
    num = re.findall('[0-9]+', tag.decode())  #lists
    for n in num: nums.append(int(n))
    #print(num)  #lists
    #nums.append(int(re.findall('[0-9]+', tag.decode())))  #lists
    #print(tag.decode().re.match('[0-9]+'))

print(sum(nums))
