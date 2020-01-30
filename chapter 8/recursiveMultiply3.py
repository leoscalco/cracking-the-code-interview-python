def minProductSolver(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1
    half = minProduct(s, bigger)

    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger

def minProduct(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return minProductSolver(smaller, bigger)

print minProduct(5, 7)