from turtle import *


def theme(canvasWidth=1000, canvasHeight=1000, canvas=(157/255, 144/255, 130/255), pen_color=(230/255, 230/255, 234/255), stroke=1, speed_value=0, tracer_value=False, hideturtle=True):
  setup(canvasWidth, canvasHeight)
  bgcolor(canvas)
  color(pen_color)
  width(stroke)
  speed(speed_value)
  tracer(tracer_value)
  hideturtle = True