"""Autograder: Counting Email from Sqlite3.

@Created: 29th Jan, 2022 at 8:27:40
@author: virosh
"""
import sqlite3

# Sqlite Methods
con = sqlite3.connect("EmailDB.sqlite")
cur = con.cursor()

# Execute Sqlite Commands in EmailDB.sqlite
cur.execute('DROP TABLE if EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open mbox.txt for emails
fname = input('Enter File: ')
if (len(fname) < 1):
    fname = '../../code3/mbox.txt'
fh = open(fname)

# Iterate and find emails
for line in fh:
    if not line.startswith('From:'): continue
    frm = line.split('@')
    org = frm[1]

    '''Check to see if email and counts are present'''
    '''if not, populate EmailDB row 'org' with emails'''
    '''and add 1 to row count each time email repeated'''

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org, count)
                    VALUES(?, 1)''', (org,))

    else:
        cur.execute('''UPDATE Counts set count = count + 1
                    WHERE org = ?''', (org,))

con.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
