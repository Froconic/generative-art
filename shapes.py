from turtle import *
# from theme import set_theme
import random
# TODO Function to draw a 5 pointed star
# TODO functions to draw a circle, a triangle, a square, a pentagon, a hexagon, a heptagon, an octagon, a nonagon, and a decagon
# TODO variables for colors to be used as the palette
# TODO Capture iterative designs
# TODO Flower of life function
# TODO create modules for each shape / technique


def draw_square(length, angle):
    for i in range(4):
        forward(length)
        left(angle)

def draw_circle(radius):
    circle(radius)

def draw_triangle(length):
    for i in range(3):
        forward(length)
        left(120)

def draw_pentagon(length):
  for i in range(5):
    fd(length)
    rt(72)

def draw_hexagon(length):
  for i in range(6):
    fd(length)
    lt(60)

def draw_heptagon(length):
  for i in range(7):
    fd(length)
    lt(51.42)

def draw_octagon(length):
  for i in range(8):
    fd(length)
    lt(45)

def draw_nonagon(length):
  for i in range(9):
    fd(length)
    lt(40)

def draw_decagon(length):
  for i in range(10):
    fd(length)
    lt(36)

def seed_of_life(length):
    for i in range(6):
      draw_circle(length)
      lt(60)
    penup()
    setpos(0, 100)
    rt(180)
    pendown()
    draw_circle(length)

def draw_art(rounds, length, angle):
    for i in range(rounds):
        draw_square(length, 90)
        left(angle)

def draw_art_2(rounds, length, angle):
    for i in range(rounds):
        draw_triangle(length)
        left(angle)

def draw_art_3(rounds, length, angle):
    for i in range(rounds):
        draw_circle(length)
        left(angle)


def draw_art_4(rounds, length, angle):
    for i in range(rounds):
        draw_star(length)
        lt(angle)

def tree(size,levels,angle):
  if levels == 0:
    color("green")
    dot(size)
    color("brown")
    
    return
  
  forward(size)
  right(angle)
  
  tree(size * .8, levels -1, angle)
  
  left(angle * 2)
  
  tree(size * .8, levels - 1, angle)

  right(angle)
  backward(size)

def draw_cross(length):
    for i in range(4):
        fd(length)
        bk(length)
        lt(90)
        fd(length)
        bk(length)
        lt(90)

def draw_star(length):
  for i in range(5):
    fd(length)
    rt(144)

def eulers(length,angle_steps,steps):
  angle = 0
  
  for i in range(steps):
    rt(angle)
    fd(length)
    angle += angle_steps

