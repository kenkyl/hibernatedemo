import mysql.connector
# import redis
import string
import random
import sys
import os

REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_PASSWORD='password'

MYSQL_HOST= os.environ.get('MYSQL_HOST') if (os.environ.get('MYSQL_HOST') is not None) else 'localhost' 
MYSQL_PORT= os.environ.get('MYSQL_PORT') if (os.environ.get('MYSQL_PORT') is not None) else '3306'
MYSQL_DB= os.environ.get('MYSQL_DB') if (os.environ.get('MYSQL_DB') is not None) else 'testdb'
MYSQL_USER= os.environ.get('MYSQL_USER') if (os.environ.get('MYSQL_USER') is not None) else 'root'
MYSQL_PASS= os.environ.get('MYSQL_PASS') if (os.environ.get('MYSQL_PASS') is not None) else 'password'
MYSQL_TABLE= 'init_object'

NUM_ITEMS = int(os.environ.get("NUM_ITEMS")) if (os.environ.get('NUM_ITEMS') is not None) else 100
ITEM_LENGTH = 250

def main():
    # connect to Redisx
    # r = redis.Redis(REDIS_HOST, REDIS_PORT, password=REDIS_PASSWORD, charset="utf-8", decode_responses=True)

    # connect to MySql
    print('loading data into mysql')
    # attempts = 0ß

    # attempt to connect to the database
    # while (True):
    #     try:
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DB,
        user=MYSQL_USER,
        password=MYSQL_PASS
     )
        # except:
        #     print('could not connect, retrying...')
        #     attempts += 1
        #     if (attempts > 500000):
        #         sys.exit('failed to connect to mysql! self-destruct!')
    print(connection)

    # create table (if it doesn't exist)
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{MYSQL_TABLE}` (
        id BIGINT UNIQUE NOT NULL,
        value1 VARCHAR(255),
        value2 VARCHAR(255),
        value3 VARCHAR(255),
        value4 VARCHAR(255),
        value5 VARCHAR(255)
    )
    """

    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit

    # with connection.cursor() as cursor:
    #     cursor.execute(create_table_query)
    #     connection.commit

    # insert data 
    items_list = []
    insert_query = f"""
    INSERT INTO {MYSQL_TABLE} (id, value1, value2, value3, value4, value5)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE id=id
    """
    print(f'inserting {NUM_ITEMS} items into MySQL')
    for i in range(NUM_ITEMS):
        item_value1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
        item_value2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
        item_value3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
        item_value4 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
        item_value5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))

        items_list.append((str(i), item_value1, item_value2, item_value3, item_value4, item_value5))
        # r.hset(f'items:{i}', mapping={'value1': item_value1, 'value2': item_value2, 'value3': item_value3, 'value4': item_value4, 'value5': item_value5})

    curson = connection.cursor()
    cursor.executemany(insert_query, items_list)
    connection.commit()

    # with connection.cursor() as cursor:
    #     cursor.executemany(insert_query, items_list)
    #     connection.commit()

    print('data load complete')
    quit()
    


if __name__ == "__main__":
    main()