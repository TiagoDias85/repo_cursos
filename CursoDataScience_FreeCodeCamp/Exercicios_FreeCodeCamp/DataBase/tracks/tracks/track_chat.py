import xml.etree.ElementTree as ET
import sqlite3

def lookup(element, key):
    child = element.find(key)
    if child is not None:
        return child.text
    return None

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

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
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Library.xml'

stuff = ET.parse(fname)
all_tracks = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_tracks))

for track in all_tracks:
    if lookup(track, 'Track ID') is None:
        continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')
    genre = lookup(track, "Genre")

    if name is None or artist is None or album is None:
        continue

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, length, rating, count, genre_id))

    conn.commit()

cur.close()
