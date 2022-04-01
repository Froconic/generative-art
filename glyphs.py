from turtle import *
from theme import theme
import random

# todo add curve function
# todo play with noise values

def glyph(size, noise):
  for y in range(300, -300, -size):
    for x in range(-500+size, 500, size):

      r = random.random()
      g = random.random()
      b = random.random()
      pencolor(r,g,b)

      originX = x + random.uniform(-size/4, size/4)
      originY = y + random.uniform(-size/4, size/4)

      startX = originX
      startY = originY

      penup()
      goto(startX, startY)
      pendown()

      for i in range(noise):
        endX = x + random.uniform(-size/4, size/4)
        endY = y + random.uniform(-size/4, size/4)
        goto(endX, endY)

        startX = endX
        startY = endY

      goto(originX, originY)
    noise += 1