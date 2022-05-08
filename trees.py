from turtle import *
from theme import theme
import random

# TOdo add function to change branch colors
# TODO add function to change branch thickness
# Todo add function to change xstarting point
# TODO Fix tree recursion

theme()

def tree(length, decrease, angle, noise = 0):
  if length > 10:
    width(length/10)
    fd(length)
    
    nextLength = length * decrease
    if noise > 0:
      nextLength *= nextLength + random.uniform(.9,1.1)
      
    leftAngle = angle + random.gauss(0,noise)
    rightAngle = angle + random.gauss(0, noise)
    
    lt(leftAngle)
    tree(nextLength, decrease, angle, noise)
    rt(rightAngle)
    
    rt(rightAngle)
    tree(nextLength, decrease, angle, noise)
    lt(leftAngle)
    
    bk(length)
