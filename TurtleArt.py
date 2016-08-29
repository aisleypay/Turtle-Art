#abstract turtle drawing

import turtle
from random import *


def random_move(turtle, distance):
#move turtle by turning at a random angle and moving forward by a random distance
  angle = uniform(-90,90)
  d = uniform(0,distance)
  turtle.left(angle)
  turtle.forward(d)
  
def randcolor():
  #return random color 
  return (randint(0,255), randint(0,255), randint(0,255))
  
def center(turtle):
  #send turtle to center without leaving a track
  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()

def random_walk(turtle, distance, steps):
#random walk
  turtle.color(randcolor(), randcolor())
  for step in range(0,steps):
    random_move(turtle, distance)  
  center(turtle)

def repeat(steps, trials):
#Repeat random_walk
  for trial in range(0,trials):
    random_walk(joe, 10, steps)

  
joe = turtle.Turtle()
joe.shape("turtle")
joe.speed(10)
turtle.colormode(255)

repeat(100, 15)

turtle.exitonclick()
