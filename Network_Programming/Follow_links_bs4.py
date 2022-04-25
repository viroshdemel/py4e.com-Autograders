#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
"""Autograder: Following Links with BeautifulSoup
@author: Virosh
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#Input and Iteration vars
c = 0
pos = 1
ent_pos = int(input('Enter Position: '))
ent_count = int(input('Enter Count: '))

# Url Selection
url = input('Select Url: ')
if len(url) < 1: url =  'http://py4e-data.dr-chuck.net/known_by_Fikret.html'  #'http://py4e-data.dr-chuck.net/known_by_Montgomery.html'
else: url = 'http://py4e-data.dr-chuck.net/known_by_Jaia.html'

html = urlopen(url).read()
s = soup(html, 'html.parser')

while c < ent_count:
    c = c + 1

    for tag in s('a'):
        if pos == ent_pos:
            url = tag.get('href')
            html = urlopen(url).read()
            s = soup(html, 'html.parser')
            print('Count:', c, 'Position:', pos, 'Retrieving:', url)
            pos = 1
            break

        else:
            pos = pos + 1

