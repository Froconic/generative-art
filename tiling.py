from turtle import *
from theme import theme
import random

# TODO add a function to increase levels on click
# TODO add a function to fill in the gaps
# Todo add a function to change shapes

red = "#D42121"
orange =  "#FF7F00"
yellow = "#F8BA00"
green = "#5EAB7A"
blue = "#6667AB"
indigo = "#3700FF"
violet = "#6F2B85"
white = "#FFFFFF"
black = "#000000"
grey = "#858585"
palette = [red, violet, yellow, green, blue, indigo, violet, white, black, grey]

def tiling(x,y,steps,levels):
  if levels == 0:
    if random.random() < .5:
      mode = "straight"
      color(palette[random.randint(0,8)])
      if mode == "straight":

  # Vertical
        if random.random() > 0.5:
          penup()
          goto(x,y - steps)
          pendown()
          goto(x, y + steps)

    # Horizontal
        else:
          penup()
          goto(x - steps, y)
          pendown()
          goto(x + steps, y)

    else:
      color(palette[random.randint(0, 8)])
      if random.random() > 0.5:
        penup()
        goto(x - steps, y - steps)
        pendown()
        goto(x + steps, y + steps)

      else:
        penup()
        goto(x - steps, y + steps)
        pendown()
        goto(x + steps, y - steps)

  else:
    steps /= 2
    levels -= 1
    tiling(x - steps,y + steps, steps, levels)
    tiling(x + steps,y + steps, steps, levels)
    tiling(x - steps,y - steps, steps, levels)
    tiling(x + steps, y - steps, steps, levels)

def reset():
  resetscreen()
  tiling(0,0,500,5)

