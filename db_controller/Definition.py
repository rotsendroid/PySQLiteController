from db_controller.SQLiteBase import *

class Definition(SQLiteBase):
    """
        Usage: data-definition part of the SQL statements (DDL)
    """

    def __init__(self, dbName):
        SQLiteBase.__init__(self, dbName)

    def create_table(self, tableName):
        """
            Checks to see if tableName already exists
            if not exists returns create table string
            (non-empty strings are True)
            if it exists returns False
        """
        self.tableName = tableName
        if not self.table_exists(self.tableName):
            return 'CREATE TABLE ' + self.tableName + '('
        else:
            return False

    def table_exists(self, table):
        """
            Checks whether a given table name exists in db,
            returns True if it exists and False if not
        """
        self.cursor.execute("SELECT count(*) FROM sqlite_master \
        WHERE type='table' AND name=?;", (table,))
        fetch = self.cursor.fetchone()

        if fetch[0] == 0:
            # table: [table] doesn't exists
            return False

        elif fetch[0] == 1:
            # table: [table] exists
            return True

    def add_column(self, name, dtype, is_primary=False, is_foreign=False, is_next=True,
                   fk_column='', fk_table='', fk_tableColumn=''):
        """
            This method adds a column name, type and other statements
            arguments:
                [name] -> column name
                [dtype] -> the type of the column
                [is_primary] -> True -> It's a primary key, call add_primary()
                [is_foreign] -> True -> It's a foreign key, call add_foreign()
                [is_next] -> False -> means that it doesn't follow another column
                [is_next] -> True -> another column follows, so a comma is added
        """

        column = self.add_name_type(name, dtype)
        if is_primary:
            column += self.add_primary()
        if is_foreign:
            column += self.add_foreign(fk_column, fk_table, fk_tableColumn)
        if is_next:
            column += ','
        else:
            column += ');'

        return column

    def add_name(self, name):
        """
            Returns the name of the column (/attribute)
        """

        return name

    def data_type(self, dtype):
        """
            data_type() returns the appropriate data type
            for the SQLite, based on the corresponding Python's
            data type, which is provided by the user with the [dtype]
            argument.

            SQLite data type can be one of the following:
                INTEGER or REAL or NULL or TEXT or BLOB
        """

        return self.switcher(dtype)

    def switcher(self, arg):
        """
            switcher() enables the user to select between
            SQLite data types

            [arg] is the [dtype] defined when data_type() is called
            [arg] can ONLY be on of the following:
                int or float or None or string or raw

            [d] is a dictionary which correlates Python data types with the
            corresponding SQLite's data types
        """

        d = {
            'int': 'INTEGER',
            'float': 'REAL',
            'None': 'NULL',
            'string': 'TEXT',
            'raw': 'BLOB'
        }

        if arg in d:
            return d.get(arg)
        else:
            print('Wrong data type provided!\nCheck it and try again')

    def add_type(self, dtype):
        """
            Returns the data type of a column name
        """

        return ' ' + self.data_type(dtype)

    def add_name_type(self, name, dtype):
        """
            This method combines the add.name() and add_type() methods
        """

        return self.add_name(name) + self.add_type(dtype)

    def add_primary(self):
        """
            Returns primary key Definition
        """

        return ' PRIMARY KEY'

    def add_foreign(self, fk_column, fk_table, fk_tableColumn):
        """
            This methods adds a foreign key
            arguments
                [fk_column] refers to the current table column which will be the
                    foreign key column
                [fk_table] refers to the table which will provide the foreign Key
                [fk_tableColumn] refers to the foreign table foreign key column
        """

        return 'FOREIGN KEY ' + fk_column + ' REFERENCES ' + fk_table + '(' + fk_tableColumn + ')'
