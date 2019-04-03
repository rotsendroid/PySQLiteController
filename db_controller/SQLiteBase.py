import sqlite3

class SQLiteBase:

    def __init__(self, dbName):
        self.dbName = dbName
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()
        self.tableName = None

    def commit_close(self):
        """
            Combines commit and close statements
        """
        self.connection.commit()
        self.connection.close()

    def show_tables(self):
        """
            Returns a list with the names of the tables
        """

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables_list = [x[0] for x in self.cursor.fetchall()]
        return tables_list

    def show_schema(self):
        """
            Shows the schema of a db
            returns a list of the schema definition statements for each table,
            like "CREATE TABLE address(addr TEXT)"
        """
        # self.cursor.execute("PRAGMA table_info('sqlite_master')")
        # you get a list of tuples like below
        # (0, 'telID', 'INTEGER', 0, None, 1),
        # (1, 'phoneNumber', 'TEXT', 0, None, 0)

        self.cursor.execute("SELECT sql FROM sqlite_master WHERE sql not NULL;")
        schema_list = [x[0] for x in self.cursor.fetchall()]
        return schema_list
