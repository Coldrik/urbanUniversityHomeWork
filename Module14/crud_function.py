import sqlite3

# connection = sqlite3.connect('./product.db')
# cursor = connection.cursor()
def initiate_db ():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def add_product():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute('INSERT INTO Users (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    # for user in users:
    #     print(f'Имя: {user[1]} | Почта: {user[2]} | Возвраст: {user[3]} | Баланс: {user[4]}')
    connection.commit()
    connection.close()
    return users
