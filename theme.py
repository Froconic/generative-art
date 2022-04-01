from turtle import *


def theme(canvasWidth=1000, canvasHeight=1000, canvas_color=(42/255, 183/255, 202/255), pen_color=(230/255, 230/255, 234/255), stroke = 1 , speed_value=0, tracer_value=False, hideturtle=True):
  setup(canvasWidth, canvasHeight)
  bgcolor(canvas_color)
  color(pen_color)
  width(stroke)
  speed(speed_value)
  tracer(tracer_value)
  hideturtle = True