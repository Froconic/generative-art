from turtle import *
import random
from watercolor import main
from theme import theme
from tiling import tiling
from nested_squares import nestedSquares
from shapes import *
from boxes import boxes
from gravel import gravel
from glyphs import glyph

# TODO add each technique to this canvas
# TODO create a sigil generator

theme()
bgpic("output.png")
tiling(0,0,500,6)
# nestedSquares(10,40,100)
color("#6667AB")
# main()
# eulers(5,1.05,100000)
# glyph(50,2)
# nestedSquares(5, 15, 100)

tracer(True)
mainloop()
