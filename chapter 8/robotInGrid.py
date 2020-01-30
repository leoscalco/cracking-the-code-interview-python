def getPath(maze, row, col, path, failedPoints):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    #
    if p in failedPoints:
        return False

    isAtOrigin = (row == 0) and (col == 0)

    if isAtOrigin or getPath(maze, row, col-1, path, failedPoints) or getPath(maze, row-1, col, path, failedPoints):
        path.append([row, col])
        return True

    failedPoints[p] = 1
    return False

def startGetting(maze):
    if maze == None or len(maze) == 0:
        return None
    failedPoints = {}
    path = []
    if getPath(maze, len(maze) - 1, len(maze[0]) -1, path, failedPoints):
        return path

    return None

maze = [
[1, 0, 0, 0],
[1, 1, 1, 0],
[0, 0, 1, 0],
[1, 1, 1, 1]
]
print startGetting(maze)