import psycopg2
import os
import sys
import json
import argparse
from psycopg2 import sql
from utility.dbUtility import DbUtility
from utility.helper import Helper

helper = Helper()
DB = DbUtility()


def _main(path, option):
    path = os.path.normpath(path)

    if not os.path.isfile(path):
        print("Invalid file path\n")
        sys.exit(1)

    db_name = 'BulkDB'
    table_name = 'bulktable'

    if DB.db_exist(db_name) and DB.table_exist(db_name, table_name):
        data = helper.read_file(path)

        if option == "update":
            DB.update_data(db_name, table_name, data)
        elif option == "update-on-conflict":
            DB.update_on_conflict(db_name, table_name, data)
        else:
            DB.insert_data(db_name, table_name, data)
    else:
        print('Create Table and DB first, then try again\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("d", help="Destination Folder")
    parser.add_argument("-o", "--option", help="operation. Default: insert",
                        choices=["insert", "update", "update-on-conflict"])

    args = parser.parse_args()
    path, option = args.d, args.option
    #print("d:", path, "-o:", option)
    _main(path, option)
