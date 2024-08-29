import sqlite3

# Подключение к БД
connection = sqlite3.connect('not_telegram.db')

# Создание объекта курсора
cursor = connection.cursor()

# Создание таблицы Users
# id       - целочисло, первичный ключ
# username - текст (не пустой)
# email    - текст (не пустой)
# age      - целое число
# balance  - целое число (не пустой)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Удаления пользователя с id=6
cursor.execute(" DELETE FROM Users WHERE id = ?", (6,))

# Подсчет количества всех пользователей
cursor.execute(" SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

# Подсчет суммы всех балансов
cursor.execute(" SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]
print(total_balance)

# Средний бал всех пользователей
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
