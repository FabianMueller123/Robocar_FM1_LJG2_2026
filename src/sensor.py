from gpiozero import LineSensor
from time import sleep 

sensor = LineSensor(14)
def detected ():
    print("Linie erkannt")

def not_detected():
    print("Linie nicht erkannt")

sensor.when_line = detected
sensor.when_no_line = not_detected
sleep(100000)