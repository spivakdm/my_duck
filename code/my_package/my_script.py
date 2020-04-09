import os

message = "Hello world, my name is %s" % os.environ['VEHICLE_NAME']
print(message)

