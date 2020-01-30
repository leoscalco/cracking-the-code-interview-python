def parens(n, left, right, current, result):

    if left == n and right == n:
        result.append(current)
        return

    if (left != n and (left - right) >= 0 ):
        parens(n, left + 1 , right, current + "(", result)
    if (right != n):
        parens(n, left, right + 1, current + ")", result)

n = 3
result = []
parens(n, 0, 0, "", result)
print result