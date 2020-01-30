def updateBits(n, m, i, j):
    allOnes = ~0

    left = allOnes << (j+1)

    right = ((1 << i) -1)

    mask = left | right

    n_cleared = m & mask
    m_shifted = m << i

    return n_cleared | m_shifted

print updateBits(int('10000000000', 2), int('10011', 2), 2, 6)