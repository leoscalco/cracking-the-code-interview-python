def nullifyRow(matrix, row):
    for j in xrange(len(matrix[0])):
        matrix[row][j] = 0

def nullifyCol(matrix, col):
    for i in xrange(len(matrix)):
        matrix[i][col] = 0

def setZeros(matrix):
    rowHasZero = False
    colHasZero = False

    # check if first row has a zero
    for j in xrange(len(matrix[0])):
        if (matrix[0][j] == 0):
            rowHasZero = True
            break

    for i in xrange(len(matrix)):
        if (matrix[i][0] == 0):
            colHasZero = True
            break

    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix[0])):
            if (matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in xrange(1, len(matrix)):
        if (matrix[i][0] == 0):
            nullifyRow(matrix, i)

    for j in xrange(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullifyCol(matrix, j)

    if(rowHasZero):
        nullifyRow(matrix, 0)

    if(colHasZero):
        nullifyCol(matrix, 0)


matrix = [
[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11],
[12, 13, 14, 15]
]

setZeros(matrix)
print matrix
