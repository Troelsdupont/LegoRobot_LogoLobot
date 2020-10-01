#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, GyroSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

def setup():
    global tank_drive, colorSensorLeft, colorSensorRight, ultra, sound, touchSensor, gyroSensor

    tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_drive.gyro = GyroSensor('in4')

    colorSensorLeft = ColorSensor('in1')
    colorSensorRight = ColorSensor('in2')

    colorSensorLeft.mode = 'COL-COLOR'
    colorSensorRight.mode = 'COL-COLOR'

    #ultra = UltrasonicSensor('in3')
    touchSensor = TouchSensor('in3')

    gyroSensor = GyroSensor('in4')
    gyroSensor.calibrate()

    sound = Sound()

def testGyro():
    #while not touchSensor.is_pressed:
        print(tank_drive.gyro.angle)

def turnDegree(direction, speed):
    gyroSensor.calibrate()
    if direction == 'left':
        tank_drive.turn_degrees(SpeedPercent(speed), 90)
    elif direction == 'right':
        tank_drive.turn_degrees(SpeedPercent(speed), -90)
    tank_drive.stop()

def turn(direction):
    gyroSensor.reset()
    sound.speak("turning " + direction)
    speed = 30
    #while not touchSensor.is_pressed:
    while 80 > abs(gyroSensor.angle):
        print(abs(gyroSensor.angle))
        if direction == 'left':
            tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
        elif direction == 'right':
            tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
    tank_drive.stop()

    #gyroSensor.reset()


#def turn22(direction):
    #print(direction)
#    degree = 90
#    speed = 15
#    if direction == 'left':
#        print(tank_drive.gyro.angle)
#        tank_drive.turn_left(speed = SpeedPercent(speed),degrees = -degree)
#        print(tank_drive.gyro.angle)
#    elif direction == 'right':
#        print(tank_drive.gyro.angle)
#        tank_drive.turn_right(speed = SpeedPercent(speed),degrees = degree)
#        print(tank_drive.gyro.angle)

if __name__ == "__main__":
    # TODO: Add code here
    setup()

    #colors=('unknown','black','blue','green','yellow','red','white','brown')
    colorLeft = ColorSensor.COLORS[colorSensorLeft.color]
    colorRight = ColorSensor.COLORS[colorSensorRight.color]

    tank_drive.stop()

    #print(colorLeft)
    #print(colorRight)
    #print(ultra.distance_centimeters)
    #print(colorSensorLeft.color)

    #sound.speak(colorRight)
    #sound.speak(colorLeft)
    #sound.speak(ultra.distance_centimeters)

    #sound.speak(colorSensorLeft.color)
    # drive in a turn for 5 rotations of the outer motor
    # the first two parameters can be unit classes or percentages.
    #while colorSensorLeft.color == 6:
    #    tank_drive.on(SpeedPercent(99), SpeedPercent(99))

    while not touchSensor.is_pressed:
        turn('right')
        turn('left')

    #testGyro()
    #turn('left')
    #turn('right')

    tank_drive.stop()
    sound.speak("lobot done")
    # drive in a different turn for 3 seconds
    #tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)
