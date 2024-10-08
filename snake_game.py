import turtle
import time
import random

# Set up the screen
window = turtle.Screen()
window.title("Realistic Snake Game")
window.bgcolor("lightblue")  # A more realistic background color
window.setup(width=600, height=600)
window.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("darkgreen")  # Realistic snake head color
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("gold")  # More realistic food color, like fruit
food.penup()
food.goto(0, 100)

segments = []

# Score
score = 0
delay = 0.1

# Functions to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# Main game loop
while True:
    window.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")  # Lighter green for the snake body
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        delay -= 0.001

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.1

    time.sleep(delay)

window.mainloop()
