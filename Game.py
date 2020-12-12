'''
Matt Faucher
CS 5001
'''

from turtle import Turtle

class Game():
    """Class that stores what would be global
    variables within the help_memory file
    """
    def __init__(self):
        # pen for counter attributes
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.color('black')
        
        # pen_lb for leaderboard attributes
        self.pen_lb = Turtle()
        self.pen_lb.hideturtle()
        self.pen_lb.penup()
        self.pen_lb.speed(0)
        self.pen_lb.color('black')
        
        # game attributes
        self.guesses = 0
        self.diff_level = 0
        self.flipped_cards = []
        self.play_cards = []
        self.name = ''