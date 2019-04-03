from db_controller.SQLiteBase import *
from db_controller.ValueNumbersException import ValueNumbersException

class Manipulation(SQLiteBase):
    """
        Usage: data-manipulation and queries generation

        Insert values by using insert_record() and insert_values()
    """

    def __init__(self, dbName):
        SQLiteBase.__init__(self, dbName)
        self.numberOfColumns = 0  # initializes at insert_record()

    def insert_record(self, tableName, *columnNames):
        """
            This method inserts dynamically the table name, the number and
            the names of columns (call insert_values() for the values)
            In order to prevent a possible SQL injection, whitespace checking
            happens for the arguments(check_whitespace() is called). All of the
            arguments have to be only one word long.

            Returns a string like below
            "INSERT INTO [tableName] ([*columnNames]) VALUES {*?}"
        """
        self.numberOfColumns = len(columnNames)
        if self.check_whitespace(tableName):
            t = tableName
        else:
            print('Insert record, error with the given table name')

        placeholders = "VALUES ({})".format(self.insert_placeholders())
        columns = "{}".format(self.insert_columns_names(*columnNames))

        ins = "INSERT INTO {} ({}) {};".format(t, columns, placeholders)

        return ins

    def insert_values(self, *values):
        record = []
        try:
            for i in values:
                if self.numberOfColumns != len(values):
                    raise ValueNumbersException(self.numberOfColumns, len(values))
                record.append(i)
        except ValueNumbersException as vne:
            print(vne)

        return tuple(record)  # check if it's empty (empty when exception raised)

    def insert_columns_names(self, *columnNames):
        """
            A helper method, called inside insert_record.
            Returns a string with the names of columns that
            are used in "INSERT INTO tableName {column_names}"
            at {columne_names} field
        """

        col = ''
        n = 0

        while n < self.numberOfColumns:
            if (n + 1) == self.numberOfColumns:
                col += '{}'.format(columnNames[n])
            elif n < self.numberOfColumns:
                col += '{},'.format(columnNames[n])
            n += 1

        return col  # check if it's empty (empty when exception raised)

    def insert_placeholders(self):
        """
            Returns a string composed of SQLite placeholders (?),
            equals to the number of columns, like that "?,?,?,?"
        """

        place = ''
        n = 0
        while n < self.numberOfColumns:

            if (n + 1) == self.numberOfColumns:
                place += '{}'.format('?')
            elif n < self.numberOfColumns:
                place += '{},'.format('?')
            n += 1

        return place

    def check_whitespace(self, text):
        whitespace = (' ', '\t', '\n')

        if any(x in text for x in whitespace):
            return False
        else:
            return True
