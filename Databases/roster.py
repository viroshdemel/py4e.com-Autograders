"""Autograder: Many Students in Many Courses.

@created: 1st Feb, 2022 at 06:15:34
@author: virosh
"""
import sqlite3
import json

# DB Create and Connect
con = sqlite3.connect('rosterdb.sqlite3')
cur = con.cursor()

# DB Table Cleanup and Setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Setup JSON File
fn = 'roster_data.json'
#fn = input('Enter File:')
#if len(fn) < 1: fn = 'roster_data.json'

# Open and Load Json Data
str_data = open(fn).read()
#print(str_data)
json_data = json.loads(str_data)
#print(json_data)

# Extract Json into DB
for entry in json_data:
    #print(entry)
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
                VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User where name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
                VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course where title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
               (User_id, Course_id, role) VALUES ( ?, ?, ? )''',
               (user_id, course_id, role))

    con.commit()

cur.executescript('''SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')

flag = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;'''

for row in cur.execute(flag):
    print(row[0])

cur.close()
