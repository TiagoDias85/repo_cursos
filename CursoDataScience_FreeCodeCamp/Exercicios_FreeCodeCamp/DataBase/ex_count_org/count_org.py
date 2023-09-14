import sqlite3

conn = sqlite3.connect('count_org.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.execute('SELECT SUM(count) FROM Counts')
total_emails = cur.fetchone()[0]


print("O total de emails enviados foram: ", total_emails)

cur.close()
