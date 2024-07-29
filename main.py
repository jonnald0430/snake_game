from tkinter import *
import random

# game, snake and food dimensions
WIDTH = 500
HEIGHT = 500
SPEED = 500
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF"
BACKGROUND = "#000000"

# snake model
class Snake:

    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        # appends initial snake size to coordinates 0,0
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0,0])
        
        # coordinates initialized for snake, rectangles for canvas are initialized
        for x, y in self.coordinates:
            # x,y represents top left, x + SPACE_SIZE and y + SPACE_SIZE represents bottom right
            square = Canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill = SNAKE, tag = "snake")
            # rectangles 
            self.squares.append(square)

# snake food model            
class SnakeFood:

    def __init__(self):
        # random x,y coordinates where food is spawned on canvas 0 to 500
        x = random.randint(0, (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        # snake food stored here
        self.coordinates = [x,y]

        # shaping the food
        Canvas.create_oval(x,y,x + SPACE_SIZE, y +
                           SPACE_SIZE, fill= FOOD,
                           tag="food")
        
