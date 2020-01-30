def paintFill(matrix, r, c, originalColor, newColor):
    if (r < 0) or (r >= len(matrix)) or (c < 0) or (c >= len(matrix)):
        return False

    if matrix[r][c] == originalColor:
        matrix[r][c] = newColor
        paintFill(matrix, r+1, c, originalColor, newColor)
        paintFill(matrix, r-1, c, originalColor, newColor)
        paintFill(matrix, r, c+1, originalColor, newColor)
        paintFill(matrix, r, c-1, originalColor, newColor)

    return True

def startPaintFill(matrix, r, c, newColor):
    if matrix[r][c] == newColor:
        return False

    paintFill(matrix, r, c, matrix[r][c], newColor)

matrix = [
[0, 0, 0, 0],
[1, 3, 4, 5],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
print startPaintFill(matrix, 1, 0, 2)
print matrix