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

# collision and movement        
def next_turn(snake, food):
    # gets x,y coordinates of snake (first element of coordinates list for snake)
    x, y = Snake.coordinates[0]

    # checks for direction of snake
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # new x,y coordinates inserted at [0] of Snake.coordinates
    Snake.coordinates.insert(0, (x,y))

    # new rectangle is created on canvas object of new x,y coordinates, color specified by fill=SNAKE
    square = Canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE)
    
    # new rectangle added to method Snake.squares
    Snake.squares.insert(0, square)

    # checks if head of snake is at the same coordinates of food object 
    if x == SnakeFood.coordinates[0] and y == SnakeFood.coordinates[1]:
        # score increments by 1 if at same coordinates
        global score
        score += 1
        # points is printed, food is deleted as snake eats it
        Label.config(text="Points:{}".format(score))
        Canvas.delete("food")
        food = SnakeFood()

    # if food isn't eaten then tail of snake is removed from coordinates and squares list
    else:
        del Snake.coordinates[-1]
        Canvas.delete(Snake.squares[-1])    
        del Snake.squares[-1]

    # if snake runs into wall or itself, game over function is called
    if check_collisions(snake):
        game_over()

    # if not, then next_turn is called again and game keeps going
    else:
        window.after(SPEED, next_turn, snake, food)
