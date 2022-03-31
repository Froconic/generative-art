from turtle import *
import random
from watercolor import main
from theme import theme
from tiling import tiling
from nested_squares import nestedSquares
from shapes import *

# TODO add each technique to this canvas

theme()
bgpic("output.png")
# tiling(0,0,500,6)
# nestedSquares(10,40,100)
color("#6667AB")
seed_of_life(100)

tracer(True)
mainloop()
