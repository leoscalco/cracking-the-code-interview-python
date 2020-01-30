import collections

l = [1, 4, 5, 7, 8, 3, 4, 4, 5, 1]
d = collections.OrderedDict()

counter = len(l)
for i in xrange(counter-1, 0, -1):
    if l[i] in d:
        l.pop(d[l[i]])
    d[l[i]] = i

print l