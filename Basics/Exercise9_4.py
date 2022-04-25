"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the
greatest number of mail messages. The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates a Python dictionary that maps
the sender's mail address to a count of the number of times they appear in the file. After the
dictionary is produced, the program reads through the dictionary using a maximum loop to find the
most prolific committer."""

counts = dict()
fn = open("mbox-short.txt")
bigcount = 0

for L in fn:
    find = L.find('From ')
    if find == 0:
        found = L[find:]
        split = found.split()
        word = split[1]
        counts[word] = counts.get(word, 0) + 1

for wd, count in counts.items():
    if count > bigcount:
        bigword = wd
        bigcount = count

print(bigword, bigcount)
