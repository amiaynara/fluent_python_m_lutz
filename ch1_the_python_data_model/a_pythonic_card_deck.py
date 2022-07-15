import collections
import random


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck():
  '''What is a french deck?'''

  def __init__(self):
    '''The constructor for french deck'''
    self.ranks = list(range(2,10)) + list('AJKQ')
    self.suits = ['heart', 'spade', 'club', 'diamond']
    self.deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

  def get_card(self):
    '''Method to return a random card, this just works because 'choice' requires a squence, 
    and implementing __get_item__ method makes the objects a sequence'''
    return random.choice(self.deck)

  def __get_item__(self, position):
    '''The dunder method that makes it a sequence'''
    return self.deck[position]

  def __len__(self):
    '''The dunder method that makes it a sequence'''
    return len(self.deck)

def main():
  '''This method will test the features of the FrenchDeck'''
  french_deck = FrenchDeck()
  card = french_deck.get_card()
  print('A random card:', card)
  
if __name__ == '__main__':
  main()
