import sqlite3


# connection = sqlite3.connect('./product.db')
# cursor = connection.cursor()
def initiate_db_product():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def initiate_db_user():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()
    connection.close()


def is_included(username) -> bool:
    """
    Вернет True если пользователь есть в таблице
    """
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    select_users = cursor.execute('SELECT username FROM Users').fetchall()
    check = False
    for select in select_users:
        check = username == select[0]
        if check:
            break

    return check



def add_product():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('./product.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    users = cursor.fetchall()
    # for user in users:
    #     print(f'Имя: {user[1]} | Почта: {user[2]} | Возвраст: {user[3]} | Баланс: {user[4]}')
    connection.commit()
    connection.close()
    return users
