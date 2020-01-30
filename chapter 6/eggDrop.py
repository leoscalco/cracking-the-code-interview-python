import math
import sys
countDrops = 0
def drop(floor):
    return floor >= nthFloor

def calculateInterval(floors):
    a = -1
    b = 1
    c = floors - 1
    d=((b^2)-4*a)*c
    m1=math.sqrt(d)
    x1=(-b+m1)/(2*a)
    x2=(-b-m1)/(2*a)
    return math.ceil(x2)

def findBreakingPoint(floors):
    interval = calculateInterval(floors)
    previousFloor = 0
    egg1 = interval
    countDrops = 1

    while not drop(egg1) and egg1 <= floors :
        countDrops += 1
        interval -= 1
        previousFloor = egg1
        egg1 += interval

    egg2 = previousFloor+1
    while egg2 < egg1 and egg2 <= floors and not drop(egg2):
        countDrops+=1
        egg2 += 1

    return -1 if egg2 > floors else egg2, countDrops

nthFloor = 99 # where the egg breaks
print findBreakingPoint(100)

