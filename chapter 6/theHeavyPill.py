arr = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.1, 1.]
weight = 0.0 # i cant check just once, so increment weight
for i in xrange(len(arr)):
    arr[i] = arr[i] * (i+1)
    weight += arr[i]

# TAKE 1 Pill, after 2 pills, 3 pills ...
# 210 = 20 * 21 / 2 -> sum of terms 1 to 20

answer = (weight - 210) / 0.1
print int(answer)
