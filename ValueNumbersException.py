
class ValueNumbersException(Exception):
    """
        An exception class raised when the number of values the user
        tries to insert are different than the number of columns,
        works with Manipulation class

        Example
        insert_values(4, 1, 'Nick', 'A St')
        exception raised, because
        1st arg->number of columns: 4
        total number of values: 3
    """

    def __init__(self, numberColumns, numberValues):
        self.numberColumns = numberColumns
        self.numberValues = numberValues

    def __str__(self):
        return "\nValueNumberException\nNumber of values tried to insert is " \
               "different than the number of columns\nNumber of values given: {}\n" \
               "Number of columns: {}".format(self.numberValues, self.numberColumns)
