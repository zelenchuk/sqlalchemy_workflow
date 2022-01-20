# from sqlalchemy import create_engine

# # 1111 это мой пароль для пользователя postgres
# engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")
# engine.connect()

# print(engine)


from dotenv import dotenv_values
config = dotenv_values(".env")


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

params = {
  'dbname': config['DB_NAME'],
  'user': config['DB_USER'],
  'password': config['DB_PASS'],
  'host': config['DB_HOST'],
  'port': config['DB_PORT'],
}

# conn = psycopg2.connect(**params)


# cur = conn.cursor()

# cur.execute("SELECT * FROM auth_user")

# # Retrieve query results
# records = cur.fetchall()
# # print(records)

# for service in records:
# 	print(service)
# 	print("="*50)


# cur.close()


# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# cursor = conn.cursor()  # Создаем курсор для выполнения операций с базой данных
# sql_create_database = cursor.execute('create database sqlalchemy_tuts')   # Создаем базу данных


# # Закрываем соединение
# cursor.close()
# conn.close()


from sqlalchemy import create_engine

a = 'postgresql+psycopg2://'+ params['user'] + ':' + params['password'] +'@' + params['host'] + ':' +params['port'] + '/' + params['dbname']

# engine = create_engine(a)



# engine.connect()

# print(engine)


print(a)