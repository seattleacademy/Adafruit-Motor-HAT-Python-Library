#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import sys

# create a default object, no changes to I2C address or frequency
# mh = Adafruit_MotorHAT(addr=0x62)
mh = Adafruit_MotorHAT(addr=int(sys.argv[1]))


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, int(sys.argv[2]))
myStepper.setSpeed(30)             # 30 RPM
myStepper.step(int(sys.argv[3]), Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
print("dataToSendBack")
print(sys.argv[1])
sys.stdout.flush()
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
# while (True):
#     print("Single coil steps")
#     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
#     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

#     print("Double coil steps")
#     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
#     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

#     print("Interleaved coil steps")
#     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
#     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

#     print("Microsteps")
#     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
#     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
