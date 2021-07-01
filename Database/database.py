from mysql.connector import connect, Error
from Database.tables import *


class Database:

    def __init__(self):
        DB_NAME = 'student_ledger'
        DATABASES = []

        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root'
        }

        self.db = connect(**config)
        self.cursor = self.db.cursor(buffered=True)
        self.cursor.execute("SHOW DATABASES")

        for database in self.cursor:
            DATABASES.append(database[0])

        if DB_NAME not in DATABASES:
            self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))

            table = Table()
            self.cursor.execute("USE {}".format(DB_NAME))
            table.createTables()

            for table_name in table.Tables:
                table_description = table.Tables[table_name]
                try:
                    self.cursor.execute(table_description)
                except Error as err:
                    print(err)
            return
        
        config['database'] = DB_NAME
        self.db = connect(**config)
        self.cursor = self.db.cursor(buffered=True)
        self.cursor.execute("USE {}".format(DB_NAME))






