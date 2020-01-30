class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getCard(self):
        return self.value + " " + self.suit

class Deck:
    def __init__(self):
        self.totalCards = 52
        self.cards = []

    def initGenericDeck(self):
        for v in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']:
            for s in ["of Hearts", "of Clubs", "of Spades", "of Diamonds"]:
                self.cards.append(Card(s, v))

    def printDeckOrder(self):
        for card in self.cards:
            print card.getCard()

deck = Deck()
deck.initGenericDeck()

deck.printDeckOrder()