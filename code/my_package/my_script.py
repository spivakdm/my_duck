import os
import RPi.GPIO
import time
from adafruit_motorki import MotorKit

message = "Hello world, my name is %s" % os.environ['VEHICLE_NAME']
print(message)
kit = MotorKit()

kit.motor1.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0
