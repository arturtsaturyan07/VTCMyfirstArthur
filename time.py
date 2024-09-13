class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for j in range(cols)] for i in range(rows)]

    def get_value(self, row, col):
        print(*self.matrix, sep='\n')
        print()
        if 0 <= row <= self.rows and 0 <= col <= self.cols:
            return self.matrix[row][col]
        else:
            return None

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def n_rows(self):
        return len(self.matrix) if self.matrix else 0

    def n_cols(self):
        return len(self.matrix[0]) if self.matrix else 0

    def delete_row(self, row):
        del self.matrix[row]

    def delete_col(self, col):
        for i in self.matrix:
            for j in range(len(i)):
                if j == col:
                    del i[j]

    def add_row(self, row):
        self.matrix.insert(row, [0 for i in range(self.cols)])
        return self.matrix

    def add_col(self, col):
        for i in range(len(self.matrix)):
            self.matrix[i].insert(col, 0)
        return self.matrix


# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(1)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()