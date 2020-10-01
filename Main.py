#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, GyroSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

def setup():
    global tank_drive, colorSensorLeft, colorSensorRight, ultra, sound, touchSensor, gyroSensor
     #g
    tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    #tank_drive.gyro = GyroSensor('in4')
    #sleep(1)
    sound = Sound()
    #tank_drive.gyro.calibrate()
    sound.speak("setup")
    colorSensorLeft = ColorSensor('in1')
    colorSensorRight = ColorSensor('in2')

    colorSensorLeft.mode = 'COL-COLOR'
    colorSensorRight.mode = 'COL-COLOR'

    #ultra = UltrasonicSensor('in3')
    touchSensor = TouchSensor('in3')

    gyroSensor = GyroSensor('in4')
    gyroSensor.calibrate()



def testGyro():
    while not touchSensor.is_pressed:
        print(tank_drive.gyro.angle)

def turn(direction, speed):
    gyroSensor.calibrate()
    sound.speak("turn " + direction)
    #gyroSensor.angle = 0

    while 90 > abs(gyroSensor.angle):
        print(abs(gyroSensor.angle))

        if direction == 'left':
            tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
        elif direction == 'right':
            tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
    tank_drive.stop()

    gyroSensor.calibrate()


def straight():
    sound.speak("straight")
    while not (colorSensorRight.color!=6 and colorSensorLeft.color!=6):
        if (colorSensorLeft.color==6 and colorSensorRight.color==6):
            tank_drive.on(SpeedPercent(10),SpeedPercent(10))
            #sound.speak(colorLeft)
            #sound.speak("Hallah white")
        if (colorSensorLeft.color!=6 and colorSensorRight.color==6) :
            tank_drive.on(SpeedPercent(12),SpeedPercent(7))
            #sound.speak(colorLeft)
            #sound.speak("Left not white")
        if (colorSensorRight.color!=6 and colorSensorLeft.color==6):
            tank_drive.on(SpeedPercent(7),SpeedPercent(12))
            #sound.speak(colorLeft)
            #sound.speak("Right not white")
        if (colorSensorRight.color!=6 and colorSensorLeft.color!=6):
            tank_drive.stop()

            break;
    tank_drive.stop()
    tank_drive.on_for_rotations(8, 8, 0.2)
    tank_drive.stop()

def place():
    sound.speak("Place")
    if (colorSensorLeft.color==6 and colorSensorRight.color==6):
        tank_drive.on(SpeedPercent(10),SpeedPercent(10))
        #sound.speak(colorLeft)
        #sound.speak("Hallah white")
    if (colorSensorLeft.color!=6 and colorSensorRight.color==6) :
        tank_drive.on(SpeedPercent(12),SpeedPercent(7))
        #sound.speak(colorLeft)
        #sound.speak("Left not white")
    if (colorSensorRight.color!=6 and colorSensorLeft.color==6):
        tank_drive.on(SpeedPercent(7),SpeedPercent(12))
        #sound.speak(colorLeft)
        #sound.speak("Right not white")
    if (colorSensorRight.color!=6 and colorSensorLeft.color!=6):
        tank_drive.on_for_rotations(10, 10, 1)
        tank_drive.on_for_rotations(-10, -10, 1)

def commandToState(commands, pointer):
    if commands[pointer]=="S":
        return 1
    if commands[pointer]=="P":
        return 2
    if commands[pointer]=="R":
        return 3
    if commands[pointer]=="L":
        return 4

def commandToState1(commands, pointer):
    if commands[pointer]=="S":
        straight()
    if commands[pointer]=="P":
        place()
    if commands[pointer]=="R":
        turn('right',10)
    if commands[pointer]=="L":
        turn('left',10)


def FSM(state):
    switcher = {
    #0: setup(),
    1: straight(),
    2: place(),
    3: turn('right',15),
    4: turn('left',15)
    }

if __name__ == "__main__":
    # TODO: Add code here


    #Setup = 0
    #Straght = "S" = 1
    #Place = "P" = 2
    #Right = "R" = 3
    #Left = "L" = 4

    # Move in an eight formation
    commands = "SRSLSLSLSLSRSRSRSRSLSLSLSLSRSRSRSRSLSLSLSLSRSRSRSRSLSLSLSLSRSRSRSRSLSLSLSLSRSRSR"
    commandPointer = 0
    state = 1
    setup()

    while True:

        commandToState1(commands, commandPointer)
        sound.speak("New state")
        sound.speak(commandPointer)

        commandPointer += 1

        if touchSensor.is_pressed:
            sound.speak("Button is is pressed")
            tank_drive.stop()
            break
