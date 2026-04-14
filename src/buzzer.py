from gpiozero import OutputDevice
from time import sleep

buzzer = OutputDevice(17)

print("OFF senden")
buzzer.off()
sleep(3)

print("ON senden")
buzzer.on()
sleep(3)

print("OFF nochmal")
buzzer.off()
sleep(3)