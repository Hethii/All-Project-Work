import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
screen.onkey(player.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # player detection of brick
    for the_car in car.all_cars:
        if the_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # player detection of the final wall
    if player.finish_line():
        player.reset_position()
        score.increase_level()
        car.level_up()


screen.exitonclick()
