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
myStepper.step(int(sys.argv[3]), int(sys.argv[4]),  Adafruit_MotorHAT.DOUBLE)