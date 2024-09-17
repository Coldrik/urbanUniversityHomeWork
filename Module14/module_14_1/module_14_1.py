import sqlite3

connection = sqlite3.connect('./not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute('CREATE INDEX')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{1}@gmail.com', i * 10, 1000))


id_counter = 1
for _ in range(6):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, id_counter))
    id_counter += 2

id_counter = 1
for _ in range(4):
    cursor.execute('DELETE FROM Users WHERE id = ?', (id_counter,))
    id_counter += 3

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возвраст: {user[3]} | Баланс: {user[4]}')


connection.commit()
connection.close()
