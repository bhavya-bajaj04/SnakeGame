from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

moving = True
while moving:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # collision with tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()


    # for seg in snake.segment:
    #     if seg == snake.head:
    #         pass
    #     elif snake.head.distance(seg) < 10:
    #         moving = False
    #         score.game_over()

screen.exitonclick()
