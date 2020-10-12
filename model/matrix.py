

#This class will represent the matrices that will be used
class Matrix:

    name: str
    columns:int
    rows: int

    # symmetrical constructor
    def __init__(self, name: str, columns: int):

        self.name = name
        self.columns = columns
        self.rows = columns

    # non-symmetrical constructor
    def __init__(self, name: str, columns: int, rows: int):

        self.name = name
        self.columns = columns
        self.rows = rows