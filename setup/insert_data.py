import mysql.connector
import string
import random
import sys
import os

MYSQL_HOST= os.environ.get('MYSQL_HOST') if (os.environ.get('MYSQL_HOST') is not None) else 'localhost' 
MYSQL_PORT= os.environ.get('MYSQL_PORT') if (os.environ.get('MYSQL_PORT') is not None) else '3306'
MYSQL_DB= os.environ.get('MYSQL_DB') if (os.environ.get('MYSQL_DB') is not None) else 'testdb'
MYSQL_USER= os.environ.get('MYSQL_USER') if (os.environ.get('MYSQL_USER') is not None) else 'root'
MYSQL_PASS= os.environ.get('MYSQL_PASS') if (os.environ.get('MYSQL_PASS') is not None) else 'password'
MYSQL_TABLE= 'init_object'
# default number of items is 100
NUM_ITEMS = int(os.environ.get("NUM_ITEMS")) if (os.environ.get('NUM_ITEMS') is not None) else 100
ITEM_LENGTH = 250
BATCH_THRESHOLD = 50000

def main():
    
    # connect to MySql
    print('loading data into mysql')

    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DB,
        user=MYSQL_USER,
        password=MYSQL_PASS
    )
        
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

    # insert data 
    num_runs = 1
    items_per_run = NUM_ITEMS
    count = 0
    odd_run = False
    insert_query = f"""
    INSERT INTO {MYSQL_TABLE} (id, value1, value2, value3, value4, value5)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE id=id
    """
    print(f'inserting {NUM_ITEMS} items into MySQL')

    # check to see if batching is needed for insert 
    if (NUM_ITEMS > BATCH_THRESHOLD):
        items_per_run = BATCH_THRESHOLD
        num_runs = (NUM_ITEMS // BATCH_THRESHOLD)
        if ((NUM_ITEMS % BATCH_THRESHOLD) > 0):
            num_runs += 1 
            odd_run = True
        print(f'batching into {num_runs} inserts; {items_per_run} items per run')

    for i in range(num_runs):
        items_list = []
        # adjust num items for last if "odd"
        if (odd_run and (num_runs-i == 1)):
            items_per_run = NUM_ITEMS - count

        # num items / num_runs 
        for j in range(items_per_run):
            item_value1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
            item_value2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
            item_value3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
            item_value4 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))
            item_value5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = ITEM_LENGTH))

            items_list.append((str(count), item_value1, item_value2, item_value3, item_value4, item_value5))
            count += 1

        cursor = connection.cursor()
        cursor.executemany(insert_query, items_list)
        connection.commit()
        print(f'insert batch #{(i+1)} with {items_per_run} items complete')

    print('data load complete')
    quit()
    


if __name__ == "__main__":
    main()