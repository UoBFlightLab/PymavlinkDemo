import time
from pymavlink import mavutil

master = mavutil.mavlink_connection("tcp:127.0.0.1:14550")

master.wait_heartbeat()

master.mav.command_long_send(
    1,1,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4,
    0,
    0,
    0,
    0,
    0
)

time.sleep(0.5)