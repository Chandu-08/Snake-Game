from turtle import Screen
import time
from Snake_body import Snake
from food import Food
from scoreboard import ScoreBoard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
Body = Snake()
food = Food()
Score_board = ScoreBoard()

# Game state variables
game_is_on = True
paused = False
speed = 0.1

# Movement controls
screen.listen()
screen.onkey(Body.move_up, "Up")
screen.onkey(Body.move_down, "Down")
screen.onkey(Body.move_right, "Right")
screen.onkey(Body.move_left, "Left")

# Pause function
def toggle_pause():
    global paused
    paused = not paused

screen.onkey(toggle_pause, "p")

# Restart function
def restart_game():
    global game_is_on, speed
    Score_board.reset()
    Body.reset()
    speed = 0.1
    game_is_on = True
    run_game_loop()

screen.onkey(restart_game, "r")

# Game loop
def run_game_loop():
    global game_is_on, speed

    while game_is_on:
        if not paused:
            screen.update()
            time.sleep(speed)
            Body.move()

            # Collision with normal food
            if Body.segments[0].distance(food) < 15:
                food.refresh()
                Body.extend()
                Score_board.increase_score()

                # Increase speed every 5 points
                if Score_board.score % 5 == 0 and speed > 0.03:
                    speed -= 0.005

            # Collision with wall
            head = Body.segments[0]
            if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
                Score_board.game_over()
                game_is_on = False

            # Collision with tail
            for segment in Body.segments[1:]:
                if Body.segments[0].distance(segment) < 10:
                    Score_board.game_over()
                    game_is_on = False
        else:
            screen.update()

run_game_loop()
screen.exitonclick()
