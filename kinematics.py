from pylab import *
from matplotlib.path import Path
import matplotlib.patches as patches
import math
import sys


def plotArm(x1, y1, xf, yf, l1, l2):
  X = np.linspace(0, 30, 256,endpoint=True)
  
  verts = [
    (0., 0.), # left, bottom
    (x1, y1), # left, top
    (xf, yf), # right, top
    ]

  codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         ]

  path = Path(verts, codes)

  fig = figure()
  ax = fig.add_subplot(111)
  patch = patches.PathPatch(path, facecolor='none', lw=2)
  ax.add_patch(patch)
  ax.set_xlim(-20,50)
  ax.set_ylim(-20,50)

  # Add the dots
  finalDot = patches.Circle((x1, y1), 1, facecolor="red", edgecolor="none")
  mediumDot = patches.Circle((xf, yf), 1, facecolor="blue", edgecolor="none")
  initialDot = patches.Circle((0, 0), 1, facecolor="yellow", edgecolor="none")
  ax.add_patch(finalDot)
  ax.add_patch(mediumDot)
  ax.add_patch(initialDot)

  # Add the circles
  l1circle = patches.Circle((0, 0), l1, facecolor="none", lw=1, edgecolor="green")
  l2circle = patches.Circle((xf, yf), l2, facecolor="none", lw=1, edgecolor="green")
  maxcircle = patches.Circle((0, 0), l1+l2, facecolor="none", lw=1, edgecolor="pink")
  mincircle = patches.Circle((0, 0), l2-l1, facecolor="none", lw=1, edgecolor="pink")
  ax.add_patch(l1circle)
  ax.add_patch(l2circle)
  ax.add_patch(maxcircle)
  ax.add_patch(mincircle)

  # Add the grid
  ax.xaxis.set_major_locator(MultipleLocator(10.0))
  ax.xaxis.set_minor_locator(MultipleLocator(1.0))
  ax.yaxis.set_major_locator(MultipleLocator(10.0))
  ax.yaxis.set_minor_locator(MultipleLocator(1.0))

  ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
  ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
  ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
  ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
  show()

def getAngles(x0, y0, l1, l2):
  xf = math.sqrt(y0**2 + x0**2)
  
  x = (l1**2 - l2**2 + xf**2)/(2*xf)

  y = math.sqrt(l1**2 - x**2)

  alfa = math.acos(x/l1)
  beta = math.asin((1/l2)*y)
  gamma = math.pi - (alfa + beta)

  dalfa = math.atan(y0/x0)

  x1 = math.cos(alfa + dalfa)*l1
  y1 = math.sin(alfa + dalfa)*l1
  
  print "Resultado: (" + str(alfa+dalfa) + ", " + str(gamma) + ")" 
  #plotArm(x1, y1, x0, y0, l1, l2)
  return (alfa+dalfa, gamma)

