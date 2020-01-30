from random import randint
arr = []

n = 40


for i in xrange(1, n):
    res = randint(1, 4)
    arr.append(res)

print arr


arr2 = []

for i in xrange(1, 30):
    res = randint(1, 4)
    arr2.append(res)

print arr2