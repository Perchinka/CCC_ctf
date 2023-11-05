import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
    )
''')

cursor.executemany('''
    INSERT INTO products (name, price, description)
    VALUES (?, ?, ?)
''', [
    ('Globlglub', 10.99, 'No one don\'t know what it is'),
    ('Bath Duck', 19.99, 'Good person to talk to'),
    ('Exploit', 29.99, 'Just Script'),
    ('RC Car', 50, 'Good for racing'),
    ('CCC{5Ql_1s_FuN!}', 1337, 'How did you find it?')
])

conn.commit()
conn.close()
