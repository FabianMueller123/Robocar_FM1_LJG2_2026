import time

import motor
import sensor


def control_direction():
    last_sensor = "middle"

    while True:
        if sensor.detected_middle():
            motor.forward()
            last_sensor = "middle"

        elif sensor.detected_left():
            motor.turn_left()
            last_sensor = "left"

        elif sensor.detected_right():
            motor.turn_right()
            last_sensor = "right"
        # to do only drvies left not slight left bc its first in the command
        elif sensor.detected_middle_left():
            motor.slight_turn_left()

        elif sensor.detected_none():
            if last_sensor == "middle":
                motor.forward()

            if last_sensor == "right":
                motor.turn_right()

            if last_sensor == "left":
                motor.turn_left()

        time.sleep(0.01)
