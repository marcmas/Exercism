class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")
        self.matrix = []

        [self.matrix.append(list(map(int, item.split()))) for item in self.matrix_string]
        
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col_matrix = []
        for row in self.matrix:
            col_matrix.append(row[index-1])
        return col_matrix
