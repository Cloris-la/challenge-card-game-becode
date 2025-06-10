from typing import List
import random
from card import Card

class Player:
    def __init__(self, name: str, turn_count:int, number_of_cards:int, history:list):
        '''
        Player lass represents a player in the card game.
        Attribute includes the player's name, 
        cards(list[Cards]): The list of cards the player has taken,
        turn_count: the number of turn the player has taken,
        number_of_cards: the number of cards the players has taken,
        history(list[Card]): all cards played by the player.
        '''
        self.name = name
        self.cards: list[Card] = [] #This saves all cards in player's hand
        self.turn_count=0 
        self.number_of_cards=0 #current number of cards in payer's hand
        self.history :list[Card] = [] # No cards played at first
        
    def play(self):
        '''
        class play means the way to play.
        randomly pick a card to player.
        Remove the card played.
        Add a history of played card.
        return all cards were played.
        '''
        play_card = random.choice(self.cards) #randomly pick a card
        self.cards.remove(play_card) #remove this card from player's hands
        self.history.append(play_card) #add this card into player's history
        self.turn_count+=1  #increse a turn of play 
        self.number_of_cards= len(play_card) #update number of cards
        print(f"{self.name} turns {self.turn_count} played: {self.number_of_cards} {self.card_icon}")
        return play_card
    
    def __str__(self):
        pass
    
    class Deck:
        '''
        Deck class means a deck of planying cards.
        Attributes:
        cards[] is the list of instances of Cards.
        Initialize a new deck.

        '''
        def __init__(self) -> None :
            '''
            INitialize a empty deck.
            '''
            self.cards : list[Card] = []

        '''
        Fills the deck with a full set of 52 unique cards.
        Each card has a value in 13 values, 
        a color in 2 colors and 1 icon in [♥, ♦, ♣, ♠].
        '''
        def fill_deck(self) -> None:
            values=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            Symbols=[("red",'♥'),
                    ('red','♦'), 
                    ('black','♣'), 
                    ('black','♠')]
            self.cards=[Card(symbol, value) for symbol in Symbols for value in values]
        '''
        Shuffles the deck of cards.
        '''
        def shuffle(self) -> None:
            random.shuffle(self.cards)
        '''
        Distribute all cards to players.
        :param players: a list of Player object to distribute to
        '''
        def distribute(self,players) -> None :
            self.players = List[Player]
            #calculate how many cards each person should get
            cards_per_person = len(self.cards) // len(players)
            #Initialize card in player's hand,
            # creat empty [] to save distribution
            distributed = [[] for _ in range(players)]
            #calculate how many cards left
            remaining_cards= len (self.cards) % len(players)
            #Distribution. Player's index starts from 0
            index = 0
            for i in range(players):
                #Limits how many cards each times to distribute
                distributed[i]=self[index:index+cards_per_person] 
                index += cards_per_person
                remaining_cards=[index:]
                return distributed, remaining_cards





            









            
            

