from turtle import *
from theme import theme
import random

def roughClouds(length, decrease, angle, noise = 0):
  if length > 10:
    fd(length)
    
    nextLength = length * decrease
    leftAngle = angle
    rightAngle = angle
    
    lt(leftAngle)
    tree(nextLength, decrease, angle, noise)
    rt(rightAngle)
    
    rt(rightAngle)
    tree(nextLength, decrease, angle, noise)
    lt(leftAngle)