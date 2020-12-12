'''
Matt Faucher
CS5001 Project
'''
from turtle import Turtle
from time import sleep

class Card:
    """Class to define a card object for the turtle
       graphics board to interact with and load
    """
    def __init__(self, x, y, gif_file):
        """Initialize the Card object to have a front
        face of a specified gif file and back of constant gif file

        Args:
            gif_file (str): name of gif file located in /gifs/
        """
        # turtle settings
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.speed(7)
        
        # x and y coordinates that the card will be placed
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.back = './card.gif' # will be the same for all cards
        self.gif_file = gif_file
        
        # state attrs
        self.visible = True
        self.current = self.back
        
        
    def check_clicked(self, x, y):
        """Function to check if card was clicked on

        Args:
            x (float): x coordinate
            y (float): y coordinate

        Returns:
            [bool]: T/F based on range of pixels
        """
        x_abs = abs(self.x - x)
        y_abs = abs(self.y - y)
        
        if self.visible == True:
            if x_abs <= 50 and y_abs <= 75:
                return True
            else:
                return False
        else:
            return False
        
        
    def flip_card(self):
        """Function to flip the card face
        """
        if self.current == self.back:
            self.current = self.gif_file
        elif self.current == self.gif_file:
            self.current = self.back
            
        self.turtle.shape(self.current)
        
        
    def hide_card(self):
        """Function to hide the card/turtle image
        """
        self.visible = False
        self.turtle.hideturtle()
        return self.visible
        
        
    def delay(self):
        """Function to delay turtle animation
        """
        sleep(1)
    
    
    def __str__(self):
        """Gives a string form of the instance

        Returns:
            [str]: string form of the card
        """
        return f'Card: Back = {self.back} Front = {self.gif_file}'
    
    
    def __eq__(self, other_card):
        """To determine equality between Card instances

        Args:
            other_card (Card): another instance of class Card

        Returns:
            [bool]: True if they are equal, equality determined by gif file name
        """
        if self.gif_file == other_card.gif_file\
            and self.coordinates != other_card.coordinates:
            return True
        else:
            return False