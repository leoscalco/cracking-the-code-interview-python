tower1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tower2 = []
tower3 = []

def moveTop(origin, destination):
    destination.append(origin.pop())

def moveDisks(n, origin, destination, buffer):
    if n <= 0:
        return

    moveDisks(n - 1, origin, buffer, destination)
    moveTop(origin, destination)
    moveDisks(n - 1, buffer, destination, origin)

moveDisks(len(tower1)-5, tower1, tower2, tower3)