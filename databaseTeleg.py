import sqlite3
import os

print("создание БД")
conn = sqlite3.connect(os.getcwd()+"/talegram.db", check_same_thread=False)
cursor = conn.cursor()
try:
    print("создание таблицы БД")
    cursor.execute("CREATE TABLE main (name text, surname text, age text, sex text)")
    conn.commit()
except Exception:
    print("таблица в БД существует")
    

def add_data(name, surname, age, sex):
    print("добавление пользователя")
    # Вставляем данные в таблицу
    cursor.execute(f"INSERT INTO main VALUES ('{name}', '{surname}', '{str(age)}', '{sex}')")
    # Сохраняем изменения
    conn.commit()