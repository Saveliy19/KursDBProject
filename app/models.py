'''файл взаимодействия с таблицами базы данных'''
from werkzeug.security import generate_password_hash
import psycopg2
from psycopg2 import Error
from config import Config

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=Config.user,
                                  # пароль, который указали при установке PostgreSQL
                                  password=Config.password,
                                  host=Config.host,
                                  database=Config.db_name)

    # Курсор для выполнения операций с базой данных
    with connection.cursor() as cursor:

        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("[INFO] Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        connection.close()
        print("[INFO] Соединение с PostgreSQL закрыто")


