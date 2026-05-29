from time import sleep

from gpiozero import LineSensor

sensor_left = LineSensor(14)
sensor_right = LineSensor(2)
sensor_middle = LineSensor(1)


def detected_left():
    return sensor_left.value == 0


def detected_right():
    return sensor_right.value == 0


def detected_middle():
    return sensor_middle.value == 0


def detected_middle_left():
    return sensor_left.value == sensor_right.value == 0
