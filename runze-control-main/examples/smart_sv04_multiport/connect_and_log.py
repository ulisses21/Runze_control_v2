import logging
import pprint
from time import sleep
from runze_control.rotary_valve import RotaryValve

# Uncomment for some prolific log statements.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.handlers[-1].setFormatter(
    logging.Formatter(fmt='%(asctime)s:%(name)s:%(levelname)s: %(message)s'))


# Constants
COM_PORT = "/dev/ttyUSB0"

# Connect to a single rotary valve.
selector_valve = RotaryValve(COM_PORT, address=0x00, position_count=6)

print(f"Syringe address: {selector_valve.get_address()}")
print(f"Syringe baud rate: {selector_valve.get_rs232_baudrate()}")
print(f"Firmware Version: {selector_valve.get_firmware_version()}")

print(f"Motor status: {selector_valve.get_motor_status}")

print(f"Move to port4")
selector_valve.move_clockwise_to_position(4)



