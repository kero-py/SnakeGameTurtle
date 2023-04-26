import turtle
import random

# global constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 1
DELAY = 100  

# define directions
directions = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# main game loop
def game_state():
    global snake_direction

    draw.clearstamps()  

    # head of snake moves towards direction
    head = snake[-1].copy()
    head[0] += directions[snake_direction][0]
    head[1] += directions[snake_direction][1]

    # check for collisions
    if head in snake or head[0] < - WIDTH / 2 or head[0] > WIDTH / 2 or head[1] < - HEIGHT / 2 or head[1] > HEIGHT / 2:
        reset()
    else:
        # keep snake moving if no collisions
        snake.append(head)

        # check if food has been eaten
        if not eat_food():
            snake.pop(0)  # snake stays the same length until food has been eaten.

        # draw snake
        for segment in snake:
            draw.goto(segment[0], segment[1])
            draw.stamp()

        # score is shown on title
        screen.title(f"Snake Game - Score: {score}")
        screen.update()

        # continue
        turtle.ontimer(game_state, DELAY)

# generate random food
def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

# position of snake and food
def get_position(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  
    return distance

# eats food upon collision; adds 1 to score when food is eaten
def eat_food():
    global food_pos, score
    if get_position(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

# resets the game
def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [0, 20], [0, 40]]
    snake_direction = "right"
    food_pos = get_random_food_pos()
    food.goto(food_pos)  
    game_state()


# set up screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  
screen.title("Snake Game Turtle")
screen.bgcolor("black")
screen.tracer(0)  

# draw using Turtle
draw = turtle.Turtle()
draw.shape("square")
draw.color("white")
draw.penup()

# key event listeners
screen.listen()
screen.onkey(up, "Up")
screen.onkey(right, "Right")
screen.onkey(down, "Down")
screen.onkey(left, "Left")

# draw food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE)  
food.penup()

# calls the reset function
reset()

# end game
turtle.done()