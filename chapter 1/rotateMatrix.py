def rotate(matrix):
    if (len(matrix) == 0):
        return False

    for layer in xrange(len(matrix) / 2):
        first = layer
        last = len(matrix) - 1 - layer
        for i in xrange(first, last):
            offset = i - first
            top = matrix[first][i]
            print top
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            print matrix[first][i]

            # bottom -> left
            matrix[last-offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return True

matrix = [
[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11],
[12, 13, 14, 15]
]

rotate(matrix)
print matrix
