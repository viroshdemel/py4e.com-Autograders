"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown
below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fi = open(name)

counts = {}
lst = []

for line in fi:
    fnd = line.find('From ')
    sv_From = line[fnd:]
    split_colon = sv_From.split(':')
    if len(split_colon) > 1:
        sv_hour = split_colon[0]
        lst.append(sv_hour[-2:])

for word in lst:
    counts[word] = counts.get(word, 0) + 1

for k,v in sorted(counts.items()):
    print(k,v)
