from pylab import *
from matplotlib.path import Path
import matplotlib.patches as patches
import math
import sys

L1=13.0
L2=22.0

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

def getAngles(xf, yf, l1, l2):

  print "Calculando para (" + str(xf) + ", " + str(yf) + ")"
  a=l2*(l2+l1)
  b=2*yf*l2
  c=l2*l1+l1**2-xf*l1-yf**2

  root = - math.sqrt(b**2 + 4*a*c)
  fi= (b + root)/(2*a)
  negfi = (b - root)/(2*a)
 
  beta = math.asin(fi)

  print "La beta seria: " + str(math.degrees(beta)) 

  x1 = xf - (1 - fi**2)*l2
  
  print "x1 seria: " + str(x1)

  alfa = math.acos(x1/l1)
  print "La alfa seria: " + str(math.degrees(alfa))

  y1 = l1 * math.sin(alfa) 

  print "Y la y1 seria entonces: " + str(y1)
  plotArm(x1, y1, xf, yf, l1, l2)

def getAngles2(x0, y0, l1, l2):
  xf = math.sqrt(y0**2 + x0**2)
  
  x = (l1**2 - l2**2 + xf**2)/(2*xf)

  y = math.sqrt(l1**2 - x**2)

  alfa = math.acos(x/l1)
  beta = math.asin((1/l2)*y)
  gamma = 180 - (alfa + beta)

  dalfa = math.atan(y0/x0)

  x1 = math.cos(alfa + dalfa)*l1
  y1 = math.sin(alfa + dalfa)*l1
  
  #print "Resultado: (" + str(alfa+dalfa) + ", " + str(gamma) + ")" 
  plotArm(x1, y1, x0, y0, l1, l2)


n=float(sys.argv[1])
m=float(sys.argv[2])

distance = (math.sqrt(m**2 + n**2))
if distance > L1 + L2:
  print "Punto fuera de alcance"
elif distance < (L2-L1):
  print "Destino en el punto ciego"
else:
  for i in xrange(50000):
    getAngles2(n,m,L1,L2)

