#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: Add code here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

colorLeftSensor = ColorSensor('in1')
colorRightSensor = ColorSensor('in2')
touchSensor = TouchSensor('in3')

colorRightSensor.mode = 'COL-COLOR'
colorLeftSensor.mode = 'COL-COLOR'

#ultra = UltrasonicSensor('in3')
rotationWheel = 5*3.14;

sound = Sound()

#colors=('unknown','black','blue','green','yellow','red','white','brown')
colorLeft = ColorSensor.COLORS[colorLeftSensor.color]
colorRight = ColorSensor.COLORS[colorRightSensor.color]

print(colorLeft)
print(colorRight)

sound.speak(colorRight)
#sound.speak(colorLeft)
#sound.speak("I am the logo  lobots")
def straight():
    if (colorLeftSensor.color==6 and colorRightSensor.color==6):
        tank_drive.on(SpeedPercent(10),SpeedPercent(10))
        #sound.speak(colorLeft)
        #sound.speak("Hallah white")
    if (colorLeftSensor.color!=6 and colorRightSensor.color==6) :
        tank_drive.on(SpeedPercent(12),SpeedPercent(7))
        #sound.speak(colorLeft)
        #sound.speak("Left not white")
    if (colorRightSensor.color!=6 and colorLeftSensor.color==6):
        tank_drive.on(SpeedPercent(7),SpeedPercent(12))
        #sound.speak(colorLeft)
        #sound.speak("Right not white")
    if (colorRightSensor.color!=6 and colorLeftSensor.color!=6):
        tank_drive.on_for_rotations(8, 8, 0.1)

def place():
    if (colorLeftSensor.color==6 and colorRightSensor.color==6):
        tank_drive.on(SpeedPercent(10),SpeedPercent(10))
        #sound.speak(colorLeft)
        #sound.speak("Hallah white")
    if (colorLeftSensor.color!=6 and colorRightSensor.color==6) :
        tank_drive.on(SpeedPercent(12),SpeedPercent(7))
        #sound.speak(colorLeft)
        #sound.speak("Left not white")
    if (colorRightSensor.color!=6 and colorLeftSensor.color==6):
        tank_drive.on(SpeedPercent(7),SpeedPercent(12))
        #sound.speak(colorLeft)
        #sound.speak("Right not white")
    if (colorRightSensor.color!=6 and colorLeftSensor.color!=6):
        tank_drive.on_for_rotations(10, 10, 1)
        tank_drive.on_for_rotations(-10, -10, 1)



while True:

    straight()
    straightpush()
        #sound.speak(colorLeft)
        #sound.speak("Right not white")
    if touchSensor.is_pressed:
        sound.speak("Button is is pressed")
        tank_drive.stop()
        break



# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
#tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

# drive in a different turn for 3 seconds
#tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)
