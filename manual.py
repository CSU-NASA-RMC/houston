# Remote manual control of robot
import inputs
import threading
import collections
import time
import logging
import remote

port = 42070 # For network

# Scales input value and rejects within a dead spot
def map(value, range):
    dead = range[0]
    range_max = range[1]

    if value <= dead and value >= -dead: # Inside dead spot
        value = 0
    else: # Actual input
        value /= abs(range_max) # Scale to unitary

    # Guarantee unitary output
    if value > 1:
        value = 1
    elif value < -1:
        value = -1

    return value


def read_output(append):
    axis = [['ABS_X', 0],       # 0 Left stick horizontal (-32768, 2604, 32767) min=left
            ['ABS_Y', 0],       # 1 Left stick vertical (-32768, 269, 32767) min=up
            ['ABS_RX', 0],      # 2 Right stick horizontal (-32768, 0, 32767) min=left
            ['ABS_RY', 0],      # 3 Right stick vertical (-32768, 1036, 32767) min=up
            ['ABS_Z', 0],       # 4 Left trigger (0, 255) min=unpressed
            ['ABS_RZ', 0],      # 5 Right trigger (0, 255) min=unpressed
            ['ABS_HAT0X', 0],   # 6 D-Pad horizontal (-1, 0, 1) min=left
            ['ABS_HAT0Y', 0]]   # 7 D-Pad vertical (-1, 0, 1) min=up

    # Used to map values to [-1, 1]. Within dead spot maps to 0
    # [dead spot, abs max]
    mappings = [[3000, 32767],  # 0
                [3000, 32767],  # 1
                [3000, 32767],  # 2
                [3000, 32767],  # 3
                [20, 255],      # 4
                [20, 255],      # 5
                [0, 1],         # 6
                [0, 1]]         # 7

    while True:
        events = inputs.get_gamepad()
        for event in events:
            logging.debug(event)

            # Axis input
            if event.ev_type == "Absolute":
                for i in range(len(axis)):
                    if axis[i][0] == event.code:
                        axis[i][1] = map(event.state, mappings[i])

            # Button input
            elif event.ev_type == "Key":
                # BTN_SOUTH = A
                # BTN_EAST = B
                # BTN_NORTH = X
                # BTN_WEST = Y
                # BTN_TL = Left bumper
                # BTN_TR = Right bumper
                # BTN_SELECT = Select, unsurprisingly
                # BTN_START = Start
                # BTN_MODE = Xbox button
                # BTN_THUMBR = Right stick click
                # BTN_THUMBL = Left stick click

                if event.state == 1:
                    print(event.code)
                    remote.send("Button") # TODO packetize

        append(axis)


def init():
    logging.info("Starting manual control")

    # This all obeys GIL so there *shouldn't* be race conditions
    buffer = collections.deque(maxlen=1) # Buffer to hold most recent values

    # Start iterator
    it = threading.Thread(target=read_output, args=(buffer.append,))
    it.daemon = True
    it.start()

    # Get axis info regularly
    while True:
        print(buffer)
        remote.send("Axis") # TODO packetize
        time.sleep(.25) # Don't overwhelm network (lowest possible is probably ~0.005 sec)


# Testing
if __name__ == "__main__":
    init()