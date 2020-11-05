import os
from dotenv import load_dotenv, find_dotenv
import psycopg2


class Connection:
    # default constructor
    def __init__(self):
        load_dotenv(find_dotenv())
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASS = os.getenv('DB_PASS')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')

    # A method to create conenction to database
    # @param :
    # self: Reference of the class
    # path: path of the location
    # db_name: optional,the name of the db to which connection should Be made.. Default: default db name from the .env file
    # Returns connection object

    def create_connection(self, db_name=''):
        db = db_name if db_name != '' else self.DB_NAME
        connection = psycopg2.connect(user=self.DB_USER,
                                      password=self.DB_PASS,
                                      host=self.DB_HOST,
                                      port=self.DB_PORT,
                                      database=db)
        return connection
