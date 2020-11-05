import psycopg2
import sys
import os
from psycopg2 import sql
from database.connection import Connection
from utility.helper import Helper

db_connection = Connection()
helper = Helper()


class DbUtility:
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    def insert_data(self, db_name, table_name, data):
        try:
            print("\nStart data insertion", end="...")

            connection = db_connection.create_connection(db_name)
            cursor = connection.cursor()

            sql = (
                f"INSERT INTO {table_name} (uuid, date, min, max, avg) VALUES (%s, %s, %s, %s, %s)")
            # Create a list of tuples
            tuples = list([(x['uuid'], x['data'], x['min'], x['max'], x['avg'])
                           for x in data])

            if not len(data) == 0:
                cursor.executemany(sql, tuples)
                connection.commit()

            cursor.close()
            connection.close()

            print("data inserted.\n")

        except (Exception, psycopg2.Error) as error:
            print('insert_data error: ' + str(error))
            sys.exit(1)

    def update_data(self, db_name, table_name, data):
        try:
            print("\nStart data updating", end="...")

            connection = db_connection.create_connection(db_name)
            cursor = connection.cursor()

            tuples = list(
                ({'uuid': x['uuid'], 'data': x['data'], 'min': x['min'], 'max': x['max'], 'avg': x['avg']} for x in data))

            sql = (f"""UPDATE {table_name} 
                   SET min = %(min)s, max = %(max)s, avg = %(avg)s
                   WHERE uuid= %(uuid)s and date = %(data)s""")

            cursor.executemany(sql, tuples)
            connection.commit()

            cursor.close()
            connection.close()

            print("data updated.\n")

        except (Exception, psycopg2.Error) as error:
            print('update_data error: ' + str(error) + '\n')
            sys.exit(1)

    def update_on_conflict(self, db_name, table_name, data):
        try:
            print("\nStart data importing", end="...")

            connection = db_connection.create_connection(db_name)
            cursor = connection.cursor()

            sql = f"""INSERT INTO 
                    {table_name} (uuid, date, min, max, avg) VALUES (%(uuid)s, %(data)s, %(min)s, %(max)s, %(avg)s)
                    ON CONFLICT(uuid, date)
                    DO UPDATE 
                    SET min = %(min)s, max = %(max)s, avg = %(avg)s"""

            tuples = list(
                ({'uuid': x['uuid'], 'data': x['data'], 'min': x['min'], 'max': x['max'], 'avg': x['avg']} for x in data))

            if not len(data) == 0:
                cursor.executemany(sql, tuples)
                connection.commit()

            cursor.close()
            connection.close()

            print("data imported\n")

        except (Exception, psycopg2.Error) as error:
            print('import_data error: ' + str(error))
            sys.exit(1)

    @ staticmethod
    def db_exist(db_name):
        try:
            connection = db_connection.create_connection()
            cursor = connection.cursor()
            inserQuery = "select exists(SELECT datname FROM pg_catalog.pg_database WHERE datname = '"+db_name+"')"
            cursor.execute(inserQuery)
            exists = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return exists
        except (Exception, psycopg2.Error) as error:
            print('db_exist error: ' + str(error))

    @ staticmethod
    def table_exist(db_name, table_name):
        try:
            connection = db_connection.create_connection(db_name)
            cursor = connection.cursor()
            inserQuery = "select exists(select * from information_schema.tables where table_name='"+table_name+"')"
            cursor.execute(inserQuery)
            exists = cursor.fetchone()[0]
            return exists
        except (Exception, psycopg2.Error) as error:
            print('table_exist error: ' + str(error))
        finally:
            cursor.close()
            connection.close()
