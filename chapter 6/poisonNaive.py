DAYS_FOR_RESULT = 7
class Bottle:
    def __init__(self, id):
        self.poisoned = False
        self.id = id

    def setPoisoned(self):
        self.poisoned = True

    def isPoisoned(self):
        return self.poisoned

class TestStrip:
    def __init__(self, id):
        self.dropsByDay = []
        self.id = id

    def sizeDropsForDay(self, day):
        while len(self.dropsByDay) <= day:
            self.dropsByDay.append([])

    def addDropOnDay(self, day, bottle):
        self.sizeDropsForDay(day)
        drops = self.dropsByDay[day]
        drops.append(bottle)

    def hasPoison(self, bottles):
        for b in bottles:
            if(b.isPoisoned()):
                return True
        return False

    def getLastWeeksBottles(self, day):
        if (day < DAYS_FOR_RESULT):
            return None
        return self.dropsByDay[day - DAYS_FOR_RESULT]

    def isPositiveOnDay(self, day):
        testDay = day - DAYS_FOR_RESULT

        if testDay < 0 or testDay >= len(self.dropsByDay):
            return False

        for d in xrange(0, testDay):
            bottles = self.dropsByDay[d]
            if(self.hasPoison(bottles)):
                return True
            return False

def runTestSet(bottles, strips, day):
    index = 0
    for bottle in bottles:
        strip = strips[index]
        strip.addDropOnDay(day, bottle)
        index = (index + 1) % len(strips)

def findPoisonedBottle(bottles, strips):
    today = 0
    while(len(bottles) > 1 and len(strips) > 0):
        runTestSet(bottles, strips, today)
        today += DAYS_FOR_RESULT
        for strip in strips:
            if(strip.isPositiveOnDay(today)):
                bottles = strip.getLastWeeksBottles(today)
                strips.remove(strip)
                break

    if len(bottles) == 1:
        return bottles[0].id

    return -1


bottles = []
strips = []

for i in xrange(100):
    bottles.append(Bottle(i))

bottles[57].setPoisoned()

for i in xrange(10):
    strips.append(TestStrip(i))

print findPoisonedBottle(bottles, strips)