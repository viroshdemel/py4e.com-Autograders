"""Autograder: Regular Expressions."""

import re

f = input('Enter File: ')

# File Selection
#print(f)
if len(f) < 1 : f = open('regex_sum_42.txt').read()
else : f = open('regex_sum_1352650.txt').read()
#print(f)

# Regex Selection
r = re.findall('[0-9]+', f)
#print(r)

# Extract into single list and print sum
v = []
for i in r : v.append(int(i))
print(sum(v))
