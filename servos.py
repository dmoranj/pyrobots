import serial
import sys
import time

#set up the serial port for action (0==COM1==ttyS0)
ser=serial.Serial('/dev/ttyACM0')
ser.baudrate=9600

def setpos(n,angle):
  #Quick check that things are in range
  if angle > 180 or angle <0:
    angle=90
    print "WARNING: Angle range should be between 0 and 180. Setting angle to 90 degrees to be safe..."
    print "moving servo "+str(n)+" to "+str(angle)+" degrees."

  byteone=int(254*angle/180)

  #Valid range is 500-5500
  offyougo=int(4000*angle/180)+4000
  #Get the lowest 7 bits
  byteone=offyougo&127
  #Get the highest 7 bits
  bytetwo=(offyougo-(offyougo&127))/128

  print "El angulo: " + str(angle)
  print "El valor normalizado es: " + str(offyougo)
  print "El valor original es " + str(byteone)
  ser.write(chr(0xAA))
  ser.write(chr(0x0C))
  ser.write(chr(0x04))
  ser.write(chr(n))
  ser.write(chr(byteone))
  ser.write(chr(bytetwo))

def setspeed(n,speed):
  #Quick check that things are in range
  if speed > 127 or speed <0:
    speed=1
    print "WARNING: Speed should be between 0 and 127. Setting speed to 1..."
    print "Setting servo "+str(n)+" speed to "+str(speed)+" out of 127."

  offyougo=speed
  byteone=offyougo&127
  #Get the highest 7 bits
  bytetwo=(offyougo-(offyougo&127))/128

  speed=int(speed)
  ser.write(chr(0xAA))
  ser.write(chr(0x0C))
  ser.write(chr(0x07))
  ser.write(chr(n))
  ser.write(chr(byteone))
  ser.write(chr(bytetwo))

def setInitialSpeeds():
  for i in range(12):
    setspeed(i, 8)

def openLeg(joints):
  setpos(joints[1], 1);
  setpos(joints[2], 180);

def closeLeg(joints):
  setpos(joints[1], 180);
  setpos(joints[2], 1);

def setInitialPosition(leg):
  setpos(leg[0], 90);
  setpos(leg[1], 90);
  setpos(leg[2], 90);

def forward(leg):
  setpos(leg[0], 60);

def backward(leg):
  setpos(leg[0], 110);

leg1 = [0, 5, 8];
leg2 = [1, 6, 10];
leg3 = [2, 7, 11];

setInitialSpeeds()
setInitialPosition(leg1);
setInitialPosition(leg2);
setInitialPosition(leg3);

time.sleep(5)

if (sys.argv[1] == "abrir"):
  openLeg(leg1)
  openLeg(leg2)
  openLeg(leg3)
elif (sys.argv[1] == "cerrar"):
  closeLeg(leg1)
  closeLeg(leg2)
  closeLeg(leg3)
else:
  while 2 > 1:
    # Open legs
    openLeg(leg1)
    openLeg(leg3)
    closeLeg(leg2)

    time.sleep(1)

    # Move forward 1
    backward(leg1)
    backward(leg3) 
    forward(leg2)

    time.sleep(1)

    # Close legs
    closeLeg(leg1)
    closeLeg(leg3)
    openLeg(leg2)

    time.sleep(1)

    # Move forward 2
    forward(leg1)
    forward(leg3)
    backward(leg2)
    time.sleep(1)
   




