def minProductSolver(smaller, bigger, memo):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    if memo[smaller] > 0:
        return memo[smaller]

    s = smaller >> 1 # divide by 2
    side1 = minProductSolver(s, bigger, memo)
    side2 = side1
    if (smaller % 2 == 1):
        side2 = minProductSolver(smaller - s, bigger, memo)

    memo[smaller] = side1 + side2
    return memo[smaller]

def minProduct(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    memo = [0] * (smaller+1)
    return minProductSolver(smaller, bigger, memo), memo

print minProduct(5, 7)[1]