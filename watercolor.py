import cairo, sys, argparse, copy, math, random

float_gen = lambda a, b: random.uniform(a, b)

# todo Colors must be in 0 -1 range for RGB
# todo Add colors by name with Copilot
# todo play with variables in main function

lavenderBlue = (205/255, 193/255, 255/255)
slateBlue = (112/255, 128/255, 144/255)
heliotropicGray = (115/255, 113/255, 252/255)
seagreen = (0/255, 240/255, 181/255)
saddlebrown = (139/255, 69/255, 19/255)
alleyorange = (255/255, 69/255, 0/255)

colors = [lavenderBlue, slateBlue, heliotropicGray, seagreen, saddlebrown, alleyorange]

randColors = []
for i in range(15):
    randColors.append((float_gen(.4,.8), float_gen(.4,.8), float_gen(.4,.8)))

def octagon(x_point, y_point, length):
  x = x_point
  y= y_point
  diagonal = length / math.sqrt(2)
  
  oct = []
  
  oct.append((x,y))
  
  x += length
  
  oct.append((x, y))

  x += diagonal
  y += diagonal
  oct.append((x, y))

  y += length
  oct.append((x, y))

  x -= diagonal
  y += diagonal
  oct.append((x, y))

  x -= length
  oct.append((x, y))

  x -= diagonal
  y -= diagonal
  oct.append((x, y))

  y -= length
  oct.append((x, y))

  x += diagonal
  y -= diagonal
  oct.append((x, y))

  return oct

def deform(shape, steps, variance):
  for i in range(steps):
    for j in range(len(shape)-1,0,-1):
      midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
      shape.insert(j, midpoint)

  return shape

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--width", default=1000, type=int)
  parser.add_argument("--height", default=1000, type=int)
  parser.add_argument("--initial", default=120, type=int)
  parser.add_argument("--deviation", default=50, type=int)
  parser.add_argument("--baseforms", default=1, type=int)
  parser.add_argument("--finalforms", default=3, type=int)
  parser.add_argument("--minshapes", default=20, type=int)
  parser.add_argument("--maxshapes", default=25, type=int)
  parser.add_argument("--shapealpha", default=.02, type=float)
  args = parser.parse_args()
  
  width, height = args.width, args.height
  initial = args.initial
  deviation = args.deviation
  baseforms = args.baseforms
  finalforms = args.finalforms
  minshapes = args.minshapes
  maxshapes = args.maxshapes
  shapealpha = args.shapealpha
  
  canvas = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
  cr = cairo.Context(canvas)
  
  cr.set_source_rgb(.9,.9,.9)
  cr.rectangle(0,0,width,height)
  cr.fill()
  
  cr.set_line_width(1)
  
  # change colors to randColors here if desired
  for p in range(-int(height*.2), int(height*1.2), 60):
    cr.set_source_rgba(random.choice(colors)[0], random.choice(colors)[1], random.choice(colors)[2], shapealpha)

    shape = octagon(random.randint(-100, width+100), p, random.randint(100,300))
    baseshape = deform(shape, baseforms, initial)

    for j in range(random.randint(minshapes, maxshapes)):
      tempshape = copy.deepcopy(baseshape)
      layer = deform(tempshape, finalforms, deviation)
      
      for i in range(len(layer)):
        cr.line_to(layer[i][0], layer[i][1])
      cr.fill()
    
    canvas.write_to_png("output.png")

if __name__ == "__main__":
    main()