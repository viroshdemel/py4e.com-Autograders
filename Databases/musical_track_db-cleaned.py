"""Autograder: Ch15, Multi-Table Database.

@created: 3rd of Feb, 2022 at 13:55:10
@author: Virosh
"""
import xml.etree.ElementTree as ET
import sqlite3

# Sqlite3 Instantiation(connection) and (code exec)
con = sqlite3.connect('tracks.sqlite')
cur = con.cursor()

# Sqlite3 Refresh Tables
cur.executescript('''
DROP TABLE if EXISTS Artist;
DROP TABLE if EXISTS Genre;
DROP TABLE if EXISTS Album;
DROP TABLE if EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

# Track Library
track_lib = input('Enter Library file: ')
if (len(track_lib) < 1):
    track_lib = '../../code3/tracks/Library.xml'

# XML Tag Structure
"""
<key>Track ID</key><integer>369</integer>
<key>Name</key><string>Another One Bites The Dust</string>
<key>Artist</key><string>Queen</string>
"""


def lookup(dict_tags, key):
    """Lookup function."""
    found = False
    for child in dict_tags:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


# XML Instantiation (parse) method and (findall)
parse_lib = ET.parse(track_lib)
dtags = parse_lib.findall('dict/dict/dict')  # findall dictionaries
print('Dict Count:', len(dtags))  # Total dicts found

# Loop Through XML and save in DB
for entry in dtags:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    title = lookup(entry, 'Title')
    length = lookup(entry, 'Total Time')

    if artist is None or genre is None or album is None or name is None:
        continue

    print('Artist:', artist, 'Genre:', genre, 'Album:', album, 'Track:', name)

    cur.execute('''INSERT or REPLACE into Artist (name)
                VALUES(?)''', (artist, ))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT or REPLACE into Genre (name)
                VALUES(?)''', (genre, ))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT or REPLACE into Album (artist_id, title)
                VALUES(?,?)''', (artist_id, album))
    cur.execute('''SELECT id FROM Album WHERE title = ?''', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT or REPLACE into Track (title, album_id, genre_id, len)
                VALUES(?,?,?,?)''', (name, album_id, genre_id, length))

    con.commit()
