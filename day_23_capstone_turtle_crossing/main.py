import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Trogger/Frurtle')
screen.tracer(0)

# initialize turtle, cars, scoreboard objects
player = Player()
garage = CarManager()
scoreboard = Scoreboard()

# listen for key input, up = turtle moves north
screen.listen()
screen.onkey(player.move, 'Up')

# set game on or off
game_is_on = True

# main game loop
while game_is_on:
     # refresh screen
     screen.update()
     time.sleep(0.1)

    # monitor number of active cars, add new cars when fewer than NUM_CARS on screen
     while len(garage.active_cars) < garage.num_cars:
          new_car = Car()

          # ensure new car will not overlap with existing car
          for car in garage.active_cars:
               while abs(new_car.ycor() - car.ycor()) <= 30:
                    new_car = Car()

          garage.active_cars.append(new_car)

     # set cars into motion
     garage.run_cars()

     # remove car after crossing screen
     for car in garage.active_cars:
          if car.xcor() <= -310:
               garage.active_cars.remove(car)
               car.hideturtle()
    
    # assign point if player reaches goal line and reset player position
     if player.ycor() >= 270:
         scoreboard.score += 1
         scoreboard.update()
         player.reset()
    
    # end game if player is hit by car
     for car in garage.active_cars:
         if car.distance(player) <= 15:
              game_is_on = False
              scoreboard.game_over()

screen.exitonclick()