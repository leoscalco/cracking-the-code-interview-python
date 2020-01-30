# 1, 2 or 3 steps
n_steps = 100

def countSteps(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return countSteps(n-1) + countSteps(n-2) + countSteps(n-3)

print countSteps(30)
