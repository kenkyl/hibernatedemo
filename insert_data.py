import mysql.connector
import redis 
import string
import random

REDIS_HOST='redis-18015.kyle-cluster.demo.redislabs.com'
REDIS_PORT=18015
REDIS_PASSWORD='password'

MYSQL_CONNECTION='localhost'
MYSQL_PORT='3306'
MYSQL_DATABASE='testdb'
MYSQL_USER='root'
MYSQL_PASSWORD='password'
MYSQL_TABLE='init_object'

NUM_ITEMS = 2000
ITEM_LENGTH = 250

def main():
    # connect to Redisx
    r = redis.Redis(REDIS_HOST, REDIS_PORT, password=REDIS_PASSWORD, charset="utf-8", decode_responses=True)

    # connect to MySql
    print('loading data into mysql')
    connection = mysql.connector.connect(
        host=MYSQL_CONNECTION,
        port=MYSQL_PORT,
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    print(connection)
    # create table (if it doesn't exist) 
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{MYSQL_TABLE}` (
        id BIGINT UNIQUE NOT NULL,
        value1 VARCHAR(255),
        value2 VARCHAR(255)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        connection.commit

    # insert data 
    items_list = []
    insert_query = f"""
    INSERT INTO {MYSQL_TABLE} (id, value1, value2)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE id=id
    """
    for i in range(NUM_ITEMS):
        item_value1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
        item_value2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))

        items_list.append((str(i), item_value1, item_value2))
        #r.hset(f'items:{i}', mapping={'value1': item_value1, 'value2': item_value2})
    with connection.cursor() as cursor:
        cursor.executemany(insert_query, items_list)
        connection.commit()

    



if __name__ == "__main__":
    main()