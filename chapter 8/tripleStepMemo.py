def countSteps(n, memo):
    if (n < 0):
        return 0
    if n == 0:
        return 1

    if memo[n] > -1:
        return memo[n]
    else:
        memo[n] = countSteps(n - 1, memo) + countSteps(n - 2, memo) + countSteps(n - 3, memo)
        return memo[n]

def startCounting(n):
    memo = [-1] * (n+1)
    return countSteps(n, memo)

print startCounting(30)