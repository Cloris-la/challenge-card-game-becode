from typing import List

class Symbol:
    '''
    class Symbol represents a card symbol with color and icon.
    Initialize a Symbol with color and icon.
    :param color and :param icon are string
    '''
    def __init__(self, color: str, icon:list):
        self.color=["red","black"]
        self.icon=["♥", "♦", "♣", "♠"]
    
    def __str__(self) -> str:
        '''
        string representation of the symbol.
        Always return a string to show the symbol's color and icon.
        '''
        return f"{self.color} {self.icon}"
                   
    '''
    class card represents a playing card which inherits from Symbol.
    '''
class Card (Symbol):
    def __init__(self, color, icon, value:str):
        '''
        Initialize a Card with color, icon, value.
        :param color:A  string like the Symbol
        :param icon: A single character in ["♥", "♦", "♣", "♠"].
        :param value: A string represents the card's value in 
        ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        '''
        super().__init__(color, icon)
        self.value=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __str__(self) ->str:
        return f"{self.color} {self.icon} {self.value}"