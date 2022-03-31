from turtle import *


def theme(canvas_width=1000, canvas_height=1000, canvas_color=(42/255, 183/255, 202/255), pen_color=(230/255, 230/255, 234/255), stroke=1, speed_value=0, tracer_value=False, hide_turtle=True):
  setup(canvas_width, canvas_height)
  bgcolor(canvas_color)
  color(pen_color)
  width(stroke)
  speed(speed_value)
  tracer(tracer_value)
  hide_turtle = True