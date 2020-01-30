def winningGameOne(p):
    return p

def winningGameTwo(p):
    f = p*p*(1-p)
    s = p*p*(1-p)
    t = p*p*(1-p)
    all_ = (p)*(p)*(p)
    return f + s + t + all_

p = float(raw_input())

if winningGameOne(p) > winningGameTwo(p):
    print "GAME 1"
else:
    print "GAME 2"]

# game 1 > game 2
# p > 3p^2 - 2p^3 / p
# 1 > 3p - 2p^2
# 2p^2 - 3p + 1 > 0
# (2p - 1)(p - 1) > 0  -> p = (2p - 1)

# 2p - 1 > 0
# p = 0.5