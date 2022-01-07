class Card:
      suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
      ranks = ["narf", "Ace", "2", "3","4","5","6","7","8","9","10","Jack","Queen","King"]

def __init__(self, suit=0, rank=0):
    self.suit = suit
    self.rank = rank

def __str__(self):
    return (self.ranks[self.rank]+" of "+self.suits[self.suit])

def cmp(self,other):
    if self.suit > other.suit: return 1
    if self.suit < other.suit: return -1
    #suits are same, check ranks
    if self.rank == 1: #self is ace
      if other.rank != 1: return 1 #self is ace, self wins
      else: return -1 #cards are both ace
    if other.rank ==1: return -1 #if other is ace, then other wins, otherwise they are the same
    if self.rank > other.rank: return 1 #self is better
    if self.rank < other.rank: return -1 #other is better
    return -1 #cards are same, but not ace

c1 = Card(2,5)
c2 = Card(3,1)
c3 = Card(1,1)
c4 = Card(3,11)
print("c1: ",c1)
print("c2: ",c2)
print("c3: ",c3)
print("c4: ",c4)

#1 means c1 is bigger, -1 means c2 is bigger or the cards are the same
print("c1 cmp c2: ",c1.cmp(c2))
print("c2 cmp c1: ",c2.cmp(c1))
print("c4 cmp c3: ",c4.cmp(c3))
print("c4 cmp c2: ",c4.cmp(c2))