from turtle import *
from theme import theme
import random

theme(canvasWidth = 600, stroke = 3)


def gravel(size,noise):
  for y in range(400,-400, -size):
      for x in range(-250, 250, size):
          penup()
          goto(x, y)
          pendown()
          angle = random.uniform(-noise, noise)
          rt(angle)
          for i in range(4):
              forward(size)
              rt(90)

          lt(angle)
      noise += 6.66

