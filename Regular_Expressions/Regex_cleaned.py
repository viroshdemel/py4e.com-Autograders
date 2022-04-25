"""Autograder: Regular Expressions."""
import re

# File Selection
f = input('Enter File: ')
if len(f) < 1 : f = open('regex_sum_42.txt').read()
else : f = open('regex_sum_1352650.txt').read()

# Regex, Convert, Print
r = re.findall('[0-9]+', f)
v = []
for i in r : v.append(int(i))
print(sum(v))
