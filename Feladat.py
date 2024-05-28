#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image
import time



class Feladat():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        #időzitő
        self.ido=StopWatch()


     def ido():
        self.ido=StopWatch()
        

    def csipog(self):
        self.ev3.speaker.beep()