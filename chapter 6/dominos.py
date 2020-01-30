numberDominos = int(raw_input("Type the number of dominos: "))
numberSquares = 64 - int(raw_input("Type the number of removed diagonally squares: "))
numberOfWhites = 32
numberOfBlacks = numberSquares - numberOfWhites

if (numberOfWhites < numberDominos or numberOfBlacks < numberDominos):
    print "Impossible. A domino always pick two squares (black and white)"
else:
    print "Possible."