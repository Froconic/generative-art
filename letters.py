from turtle import *
from theme import theme
import random

theme(canvasWidth = 1200, canvasHeight = 800, stroke = 3)

size = 80
noise = 2
for y in range(-300,300, -size):
  for x in range(-400,400, size):
    
    px = x + random.uniform(-size/4, size/4)
    py = y + random.uniform(-size/4, size/4)
    
    px_start = px
    py_start = py
    
    penup()
    goto(px_start, py_start)
    pendown()
    
    for i in range(noise):
      px_end = x + random.uniform(-size/4, size/4)
      py_end = y + random.uniform(-size/4, size/4)
      goto(px_end, py_end)
      
      px_start = px_end
      py_start = py_end
      
    goto(px,py)


tracer(True)
exitonclick()