nDoors = 100
# False -> locked True -> opened
arr = [True] * nDoors # first pass

def passInArr(s, e, iterator):
    for i in xrange(s, e, iterator):
        arr[i-1] = not arr[i-1]

for i in xrange(2, nDoors): # starts in two and goes to n
    passInArr(i, nDoors, i) # all the others passes

for i in xrange(len(arr)):
    print i+1, arr[i]