'''
Matt Faucher
Project Memory Game

File to hold the x,y coordinates used for the card grid
all difficulty lists stored within difficulty dictionary
'''
# cards start at top left of grid
# card coordinates are based on center of the shape

easy = [
            (-305, 180), (-195, 180), (-85, 180), (25, 180),
            (-305, 20), (-195, 20), (-85, 20), (25, 20)
        ]

medium = [
            (-360, 180), (-250, 180), (-140, 180), (-30, 180), (80, 180),
            (-360, 20), (-250, 20), (-140, 20), (-30, 20), (80, 20)
         ]

hard = [
            (-415, 180), (-305, 180), (-195, 180), (-85, 180), (25, 180), (135, 180),
            (-415, 20), (-305, 20), (-195, 20), (-85, 20), (25, 20), (135, 20)
        ]

difficulty = {
                1: easy,
                2: medium,
                3: hard
             }