from turtle import *
from theme import theme
import random
import math

theme(canvasWidth=1600, stroke=3)

size = 50
noise = 0.0

def boxes(size,noise):
  for y in range(400, -400, -size):
      for x in range(-800, 800, size):
          penup()
          goto(x, y)
          pendown()

          max_distance = math.sqrt(800**2 + 400**2)
          distance = math.sqrt((x**2) + 2**2 * (y**2))
          noise =  (max_distance - distance) / 15
          noise = noise if noise > 15 else 0
          angle = random.uniform(-noise, noise)
          rt(angle)

          for i in range(4):
              forward(size)
              rt(90)

          lt(angle)
