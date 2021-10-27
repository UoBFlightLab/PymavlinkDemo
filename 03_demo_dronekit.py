import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

vehicle = connect("tcp:127.0.0.1:14550", wait_ready=True)

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.armed:
    # Wait for vehicle to arm
    time.sleep(0.5)

print("Vehicle armed")

takeoff_altitude = 20

vehicle.simple_takeoff(takeoff_altitude)

while abs(takeoff_altitude - vehicle.location.global_relative_frame.alt) > 0.5:
    pass

print("Takeoff complete")

target = LocationGlobalRelative(51.4232303,-2.6710604,100)
vehicle.simple_goto(target)

time.sleep(1.0)

vehicle.close()