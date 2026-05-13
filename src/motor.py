import board
from adafruit_pca9685 import PCA9685
import time
import logging

log = logging.getLogger(__name__)

# create I²C bus interface
i2c = board.I2C()
# create PCA9685 instance
pca = PCA9685(i2c)

current_speed_front_left = 0
current_speed_front_right = 0
current_speed_rear_left = 0
current_speed_rear_right = 0


def init():
    log.info("initialize the PWM module")
    pca.frequency = 50
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0
    pass


def stop_all():
    global current_speed_front_left, current_speed_front_right, current_speed_rear_left, current_speed_rear_right
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0
    current_speed_front_left = 0
    current_speed_front_right = 0
    current_speed_rear_left = 0
    current_speed_rear_right = 0
    
    
def front_left(speed=0):
    global current_speed_front_left
    if abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return
    
    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_left = speed
    
    if speed >= 0:
        pca.channels[0].duty_cycle = 0
        pca.channels[1].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[0].duty_cycle = motor_speed
        pca.channels[1].duty_cycle = 0
        
        
def front_right(speed=0):
    global current_speed_front_right
    if abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return
    
    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_right = speed
    
    if speed >= 0:
        pca.channels[2].duty_cycle = 0
        pca.channels[3].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[2].duty_cycle = motor_speed
        pca.channels[3].duty_cycle = 0
        
        
def rear_left(speed=0):
    global current_speed_rear_left
    if abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return
    
    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_left = speed
    
    if speed >= 0:
        pca.channels[4].duty_cycle = 0
        pca.channels[5].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[4].duty_cycle = motor_speed
        pca.channels[5].duty_cycle = 0
        
        
def rear_right(speed=0):
    global current_speed_rear_right
    if abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return
    
    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_right = speed
    
    if speed >= 0:
        pca.channels[6].duty_cycle = 0
        pca.channels[7].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[6].duty_cycle = motor_speed
        pca.channels[7].duty_cycle = 0
        
        
init() 
front_left(50)
time.sleep(3)
stop_all()