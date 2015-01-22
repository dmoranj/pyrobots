import sys
import kinematics as kin
import math
import servos as serv

L1=13.0
L2=22.0

def normalize(angle, minValue, maxValue, total):
  return angle*((maxValue-minValue)/total) + minValue

n=float(sys.argv[1])
m=float(sys.argv[2])
p=float(sys.argv[3])

print "Setting leg to (x, y, z): (" + str(n) + ", " + str(m) + ", " + str(p) + ")"
radians = kin.getAngles(n, p, L1, L2)

angles = (360/(2*math.pi))*radians[0], (360/(2*math.pi))*radians[1]

print "The final angles are (alfa, beta): (" + str(angles[0]) + ", " + str(angles[1]) + ")"

alphaClean=normalize(angles[0], 165, 40, 180)
betaClean=normalize(angles[1], 0, 220, 180)

print "The normalized values are (alpha, beta): (" + str(alphaClean) + ", " + str(betaClean) + ")"

serv.setpos(1,alphaClean)
serv.setpos(2,betaClean)

