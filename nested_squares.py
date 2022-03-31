from turtle import *
from theme import theme
import random

def draw_square(x, y, size):
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(size)
        left(90)
        
def nestedSquares(noise,shrink, size):
  for x in range(-500+size//2, 500, size):
    for y in range(-500+size//2, 500, size): 
      draw_square(x, y, size)
      
      xOff = random.uniform(-noise, noise)
      yOff = random.uniform(-noise, noise)
      
      for i in range (6):
        draw_square(x+i*xOff, y+i*yOff, size-i*shrink)
