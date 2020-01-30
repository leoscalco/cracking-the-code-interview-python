def makeChange(amount, denoms, index, hash):
    if hash[amount][index] > 0:
        return hash[amount][index]

    if index >= (len(denoms)-1):
        return 1

    denomAmount = denoms[index]
    ways = 0
    i = 0
    while i * denomAmount <= amount:
        amountRemaining = amount - i * denomAmount
        ways += makeChange(amountRemaining, denoms, index + 1, hash)
        i+=1
    hash[amount][index] = ways
    return ways

def startMakeChange(n):
    denoms = [25, 10, 5, 1]
    hash = {}
    for i in xrange(n+1):
        hash[i] = [0] * len(denoms)
    return makeChange(n, denoms, 0, hash)

print startMakeChange(10)