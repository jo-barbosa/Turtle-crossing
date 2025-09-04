import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
count = 0
while game_is_on:
    if player.ycor() > 280:
        player.reset_position()
        car_manager.reset_cars()
        scoreboard.increase_score()

    # for car in car_manager.all_cars:
    #     if car.distance(player) < 20:
    #         game_is_on = False
    #         scoreboard.game_over()
    #     break
    #
    #ALTERNATIVE TO DETECT COLLISION
    if len(car_manager.all_cars) > 5:
        for car in car_manager.all_cars:
            if abs(car.ycor() - player.ycor()) < 30:
                if abs(car.xcor() - player.xcor()) < 30:
                    game_is_on = False
                    scoreboard.game_over()
                break


    if count % 6 == 0:
        car_manager.create_car()
    count += 1
    car_manager.move_cars()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()