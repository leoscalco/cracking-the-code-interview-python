GRID_SIZE = 8
def isValid(columns, row1, col1):
    row2 = 0
    while row2 < row1:
        col2 = columns[row2]

        if col2 == col1:
            return False

        columnDistance = abs(col2 - col1)
        rowDistance = row1 - row2
        if(rowDistance == columnDistance):
            return False
        row2+=1

    return True

def addQueen(row, columns, results):
    if (row == GRID_SIZE):
        results.append(columns[:])
    else:
        for col in xrange(GRID_SIZE):
            if(isValid(columns, row, col)):
                columns[row] = col # place queen
                addQueen(row+1, columns, results)

results = []
print addQueen(0, [0]*8, results)
for a in results:
    print "( r, c )"
    for j in xrange(len(a)):
        print "(%d, %d)" % (j, a[j])
    print " "