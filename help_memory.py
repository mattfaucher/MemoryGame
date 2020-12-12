'''
Matt Faucher
CS5001 Project
Functionality for Memory game
'''

import turtle
import os
import random
import json
from Card import Card
from Game import Game
import card_locations


# Global Game object
GAME = Game()

################################## Game Controller Function ############################################

def game_controller():
    """Function to handle running of Memory Game functionality
    """
    # Generate the window for the game + leaderboard file
    window = create_game_window('Memory Game', 800, 1000)
    create_leaderboard_file()
    
    # Get users name and difficulty level
    GAME.name, GAME.diff_level = start_input(window)
    
    # draw sections of board
    draw_sections_controller(window)
    
    # add all cards to window shapes list
    cards = add_all_cards(window)
    
    # Draw the cards onto the board
    game_cards = create_card_pairs(GAME.diff_level, cards)
    # set the current cards in play
    GAME.play_cards = draw_cards(game_cards, GAME.diff_level)

    # allow user to play the game
    window.onscreenclick(clicked)
    
    # run mainloop to play the game
    window.mainloop()
    
################################## Drawing + Game Start Functions ############################################
    
def start_input(window: turtle.Screen()):
    """Function to create popup windows at start of game

    Args:
        window (turtle.Screen): turtle.Screen object

    Returns:
        string, int: returns string for name and int for difficulty level 
    """
    name = window.textinput('Welcome!', 'Please enter your name: ')
    while len(name) < 1:
        name = window.textinput('Welcome!', 'Please enter a valid name: ')
    num_cards = window.numinput('Difficulty Level', 'Please enter a number 1-3 (1 is easiest): ')
    while num_cards not in {1, 2, 3}:
        num_cards = window.numinput('Difficulty Level', 'Oops looks like you entered ' + 
                                    'something other than 1-3, please try again: ')
        
    return name, int(num_cards)


def create_game_window(title: str, height: int, width: int):
    """Function to generate the game window

    Args:
        title (str): title for bar of window
        height (int): height of the window
        width (int): width of the window

    Returns:
        [type]: [description]
    """
    # create game board
    window = turtle.Screen()
    window.setup(width, height)
    window.title(title)
    window.bgcolor('#C9D7E1')
    
    return window


def draw_sections_controller(window: turtle.Screen):
    """Function to call functions that perform drawing
    """
    # draw sections of board
    sections = turtle.Turtle()
    # hide cursor
    sections.hideturtle()
    draw_sections(sections)
    
    # draw out leaderboard
    draw_leaderboard()
    
    #draw the quit icon
    quit_icon = turtle.Turtle()
    window.addshape('./surrender.gif')
    draw_image(quit_icon, './surrender.gif', 320, -280)


def draw_sections(t: turtle.Turtle()):
    """Function to draw out the necessary areas on the board using
    draw_rectange() and add_header()

    Args:
        t (turtle.Turtle): turtle object
    """
    # pen settings and remove animations
    t.shape('classic')
    t.speed(0)
    t.pensize(4)
    
    # card section and header
    draw_rectangle(t, -480, 380, 680, 600)
    add_header(t, -260, 340, 'Card Selection', 'blue', 30)
    t.color('yellow')
    
    # leaderboard section and header
    draw_rectangle(t, 250, 380, 220, 600)
    add_header(t, 300, 360, 'Leaderboard', 'blue', 18)
    t.color('red')
    draw_leaderboard()
    
    # move counter section and header
    draw_rectangle(t, -440, -240, 600, 100)
    add_header(t, -215, -265, 'Move Counter', 'blue', 20)
    t.color('black')
    
    # add header for quit_icon
    add_header(t, 320, -370, 'QUIT', 'red', 16)


def draw_rectangle(t: turtle.Turtle(), start_x: int, start_y: int, width: int, height: int):
    """Function to draw a rectangular area on the board

    Args:
        t (turtle.Turtle): turtle object
        start_x (int): starting x coordinate
        start_y (int): starting y coordinate
        width (int): width of rectangle
        height (int): height of rectangle
    """
    t.penup()
    t.goto((start_x, start_y))
    t.pendown()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.penup()


def add_header(t: turtle.Turtle(), x: int, y: int, text: str, color: str = 'black', font_size: int = 12):
    """Function to add headers to the necessary sections
    in the game board

    Args:
        t (turtle.Turtle): turtle object
        x (int): x coordinate
        y (int): y coordinate
        text (str): text to be written
        color (str): color of the text defaults to black
        font_size (int): size of the font default to 12
    """
    t.goto(x, y)
    t.color(color)
    t.write(text, align='left', font= ('Courier', font_size, 'underline'))


def draw_image(t: turtle.Turtle(), img: str, x: int, y: int):
    """Function to draw an image to the board

    Args:
        t (turtle.Turtle): turtle object
        img (str): file name
        x (int): x coordinate
        y (int): y coordinate
    """
    t.shape(img)
    t.speed(0)
    t.penup()
    t.goto(x, y)
    return t.stamp()

################################## Generating Cards Functions ############################################

def add_all_cards(window: turtle.Screen):
    """function to create a list of all gif images
    in the ./gifs folder
    
    Args:
        window: turtle.Screen() instance

    Returns:
        [list]: list of gif images
    """
    # list to hold card names
    cards = []
    # path to folder
    gif_folder = './gifs/'
    
    # add each file to list
    for gif in os.listdir(gif_folder):
        if os.path.isfile(os.path.join(gif_folder, gif)):
            gif = os.path.join(gif_folder, gif)
            if gif.endswith('.gif'):
                cards.append(gif)
                # add gif to window shapes
                window.addshape(gif)
                
    # add default card gif
    window.addshape('./card.gif')
                
    return cards


def create_card_pairs(diff_level: int, cards: list):
    """Function to generate a list of card pairs to be used
    when drawing the game board

    Args:
        diff_level (int): difficulty level int entered by user
        cards (list): file names for all cards

    Returns:
        [list]: shuffled list of card pairs with length dependent
        on the difficulty level
    """
    
    game_cards = []
    num = 0
    
    # use num to determine how many cards to make pairs
    if diff_level == 1:
        num = 2
    elif diff_level == 2:
        num = 1
    else:
        num = 0
    
    # create list of card pairs
    for i in range(len(cards) - num):
        game_cards.append(cards[i])
        game_cards.append(cards[i])
    
    # shuffle the list of pairs
    random.shuffle(game_cards)
    
    return game_cards


def draw_cards(game_cards: list, diff_level: int):
    """Function to draw the cards to the game board

    Args:
        game_cards (list): list of files that are randomly ordered
        diff_level (int): difficulty level indicated by user
        
    Returns:
        (list): card objects that are in play
    """
    cards_in_play = []
    
    for i in range(len(game_cards)):
        # set coordinates from locations file
        x = card_locations.difficulty[diff_level][i][0]
        y = card_locations.difficulty[diff_level][i][1]
        card = Card(x, y, game_cards[i])
        # append to new list
        cards_in_play.append(card)
        card.turtle.shape(card.current)
        card.turtle.goto(x, y)
    
    return cards_in_play
        
################################## Game Logic Functions ############################################

def clicked(x: float, y: float):
    """Function to get current click coordinates and pass those
    to other functionality

    Args:
        x (float): x coordinate on page
        y (float): y coordinate on page

    """
    # check if click on quit icon
    check_for_quit(x, y)
    
    # loop through cards in play and check clicked
    for card in GAME.play_cards:
        if card.check_clicked(x, y) == True:
            # flip if clicked on card
            card.flip_card()
            # check for a match
            check_pair_match(card)
            # update guesses area
            draw_guesses()
            
    # check if game is over
    check_game_over()
        

def check_for_quit(x, y):
    """Function to check if user clicked the quit icon

    Args:
        x (float): x coordinate
        y (float): y coordinate
    """
    if x >= 305 and x <= 385 and y >= -355 and y <= -265:
        q = turtle.Screen().numinput('Quit the game?', "Would you like to quit? Enter 1 to quit, 2 to continue: ", 1, 1, 2)
        if q == 1:
            quit()
        elif q == 2:
            return
        

def check_pair_match(card: Card):
    """Function to check if the two flipped cards are a match

    Args:
        card (Card): card in GAME.play_cards
    """
    # append card to GAME.flipped_cards
    if not GAME.flipped_cards:
        GAME.flipped_cards.append(card)
    # Check for a match
    elif GAME.flipped_cards:
        if GAME.flipped_cards[0].__eq__(card):
            card.hide_card()
            GAME.flipped_cards[0].hide_card()
            GAME.flipped_cards.clear()
            GAME.guesses += 1
        elif not GAME.flipped_cards[0].__eq__(card):
            GAME.flipped_cards[0].delay()
            GAME.flipped_cards[0].flip_card()
            card.flip_card()
            GAME.flipped_cards.clear()
            GAME.guesses += 1
        else:
            card.flip_card()


def check_game_over():
    """Function to check if the game has ended and all
    matches have been found
    """
    not_visible = []
    for card in GAME.play_cards:
        if card.visible == False:
            not_visible.append(card.visible)
        else:
            continue
        
    if len(not_visible) == len(GAME.play_cards):
        window = card.turtle.screen
        play = window.textinput("Game Over!", "Would you like to play again? (Y/N): " )
        if play.upper() == 'Y':
            # update leaderboard before restarting
            update_leaderboard()
            # reset guesses
            GAME.guesses = 0
            game_controller()
        else:
            # update leaderboard before quiting
            update_leaderboard()
            quit()


def draw_guesses():
    """Function to update the move + guess counter
    """
    # settings for pen
    GAME.pen.penup()
    GAME.pen.speed(0)
    GAME.pen.goto(-135, -300)
    GAME.pen.hideturtle()
    
    # initialize the text
    pairs_found = 0
    text = f"Guesses: {GAME.guesses} ---- Matches: {pairs_found}"
    
    GAME.pen.write(text, align='center', font=('Courier', 20, 'bold'))
    
    # check for pairs found
    not_visible = []
    for card in GAME.play_cards:
        if card.visible == False:
            not_visible.append(card.visible)
    
    # save num of pairs found
    pairs_found = len(not_visible) // 2

    # clear what's been written and update
    GAME.pen.clear()
    text = f"Guesses: {GAME.guesses} ---- Matches: {pairs_found}"
    GAME.pen.write(text, align='center', font=('Courier', 20, 'bold'))
    
################################## Leaderboard Functions ############################################

def create_leaderboard_file():
    """Function to generate a leaderboard JSON file
    if one doesn't already exist in the directory
    """
    if not os.path.exists('./leaderboard.json'):
        try:
            with open('./leaderboard.json', 'w') as lb:
                data = {}
                for i in range(3):
                    data[i + 1] = []
                json.dump(data, lb, indent=4)
                
        except FileNotFoundError:
            print("File couldn't be found")
    else:
        return

        
def update_leaderboard():
    """Function to update the leaderboard json file
    """
    # read current data
    with open('./leaderboard.json', 'r') as lb:
        data = json.load(lb)
    
    # create a new dict for new game
    new = {}
    new["name"] = GAME.name
    new["score"] = GAME.guesses
        
    data[str(GAME.diff_level)].append(new)
    
    lb_sorted = sort_leaderboard(data)
    
    # write new data to the file
    with open('./leaderboard.json', 'w') as lb:
        json.dump(lb_sorted, lb, indent=4)
        
        
def sort_leaderboard(data: dict):
    """Function to sort the leaderboards using sorted lambda
    in an ascending order (lowest score = best)

    Args:
        data (dict): leaderboard.json dict file

    Returns:
        [dict]: sorted dictionary of leaderboards
    """
    one = data["1"]
    data["1"] = sorted(one, key = lambda i: i['score'])
    
    two = data["2"]
    data["2"] = sorted(two, key = lambda i: i['score'])
    
    three = data["3"]
    data["3"] = sorted(three, key = lambda i: i['score'])
    
    return data
   

def draw_leaderboard():
    """Function to write the appropriate leaderboard
    onto the screen
    """
    # read the json file
    with open('./leaderboard.json', 'r') as lb:
        data = json.load(lb)
    
    # determine which leaderboard to reference
    if GAME.diff_level == 1:
        lvl = 8
    elif GAME.diff_level == 2:
        lvl = 10
    else:
        lvl = 12
    
    # set data to the diff_level list
    data = data[str(GAME.diff_level)]
    # clear previous leaderboard draws, if any
    GAME.pen_lb.clear()
    GAME.pen_lb.goto(360, 340)
    GAME.pen_lb.color('purple')
    GAME.pen_lb.write(f'(For {lvl} cards)', align='center', font=('Courier', 16, 'italic'))
    GAME.pen_lb.color('black')

    # determine how to loop through the list based on its length
    if len(data) < 1:
        return
    elif len(data) < 6:
        loop_write(data, len(data))
    else:
        loop_write(data, 6)
            

def loop_write(data, n: int):
    """Function to loop through and write for leaderboard

    Args:
        data (list): sorted list of scores
        n (int): max length for range
    """
    # initialize variables
    y = 20
    text = ''
    for i in range(0, n):
            num = f'{i + 1}'
            name = data[i]["name"]
            score = data[i]["score"]
            text = f"{num}. {name} : {score} moves"
            GAME.pen_lb.goto(255, 320 - (y * i))
            GAME.pen_lb.color('black')
            GAME.pen_lb.write(text, align='left', font=('Courier', 14, 'bold'))