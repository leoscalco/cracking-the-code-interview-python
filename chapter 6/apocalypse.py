import random
def runOneFamily():
    boys = 0
    girls = 0
    while girls == 0:
        if random.uniform(0, 1) > 0.5:
            girls+=1
        else:
            boys+=1
    return girls, boys

def runNFamilies(n):
    boys = 0
    girls = 0
    for i in xrange(n):
        genders = runOneFamily()
        girls += genders[0]
        boys += genders[1]
    return girls / float(girls + boys)

print runNFamilies(100000000) # with n large, get close to 0.5