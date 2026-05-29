import logging
import time

import motor
import sensor

motor.init()

log = logging.getLogger(__name__)

while True:

    if sensor.detected_middle():
    motor.forward()

    elif sensor.detected_left():
    motor.turn_right()

    elif sensor.detected_right():
    motor.turn_left()

    elif sensor.detected_middle_left():
    motor.slight_turn_right()

    time.sleep(0.01)
