# Remote manual control of robot
import inputs
import threading
import collections
import time
import logging
import remote

port = 42070 # For network

control_map = 'Easy' # ('Easy', 'Advanced') Control mode, determines button mapping

# Scales input value and rejects within a dead spot
def map_unit(value, range):
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

def map_axis(axis):
    # 0 'ABS_X'       Left stick horizontal   -1=left
    # 1 'ABS_Y'       Left stick vertical     -1=up
    # 2 'ABS_RX'      Right stick horizontal  -1=left
    # 3 'ABS_RY'      Right stick vertical    -1=up
    # 4 'ABS_Z'       Left trigger            0=unpressed
    # 5 'ABS_RZ'      Right trigger           0=unpressed
    # 6 'ABS_HAT0X'   D-Pad horizontal        -1=left
    # 7 'ABS_HAT0Y'   D-Pad vertical          -1=up

    global control_map

    response = "axis," + control_map

    for i in axis:
        response += ","+str(i[1])

    return response # Sent to CAM

def map_btn(btn, state):
    # BTN_SOUTH     A
    # BTN_EAST      B
    # BTN_NORTH     X
    # BTN_WEST      Y
    # BTN_TL        Left bumper
    # BTN_TR        Right bumper
    # BTN_SELECT    Select, unsurprisingly
    # BTN_START     Start
    # BTN_MODE      Xbox button
    # BTN_THUMBR    Right stick click
    # BTN_THUMBL    Left stick click

    global control_map

    response = "btn,{},{},{}".format(control_map, btn, state)

    return response # Sent to CAM


# Spawns as iterator thread
def read_output(append):
    # Holds last value of axis
    axis = [['ABS_X', 0],       # 0 Left stick horizontal (-32768, 2604, 32767) min=left
            ['ABS_Y', 0],       # 1 Left stick vertical (-32768, 269, 32767) min=up
            ['ABS_RX', 0],      # 2 Right stick horizontal (-32768, 0, 32767) min=left
            ['ABS_RY', 0],      # 3 Right stick vertical (-32768, 1036, 32767) min=up
            ['ABS_Z', 0],       # 4 Left trigger (0, 255) min=unpressed
            ['ABS_RZ', 0],      # 5 Right trigger (0, 255) min=unpressed
            ['ABS_HAT0X', 0],   # 6 D-Pad horizontal (-1, 0, 1) min=left
            ['ABS_HAT0Y', 0]]   # 7 D-Pad vertical (-1, 0, 1) min=up

    # Range to map values to [-1, 1]. Within dead spot of 0 maps to 0
    # [dead spot, abs max]
    mappings = [[3000, 32767],  # 0
                [3000, 32767],  # 1
                [3000, 32767],  # 2
                [3000, 32767],  # 3
                [20, 255],      # 4
                [20, 255],      # 5
                [0, 1],         # 6
                [0, 1]]         # 7

    # Event handler loop
    while True:
        events = inputs.get_gamepad() # Poll controller
        for event in events:
            logging.debug(event)

            # Axis input
            if event.ev_type == "Absolute":
                for i in range(len(axis)):
                    if axis[i][0] == event.code:
                        axis[i][1] = map_unit(event.state, mappings[i])

            # Button input
            elif event.ev_type == "Key":
                if event.state == 1: # 1 = press, 0 = release

                    # Exit manual mode
                    if event.code == 'BTN_SELECT':
                        print("Exiting manual mode")
                        remote.send("STOP", port) # Stop command
                        return

                    # Toggle Easy vs Advanced mode
                    elif event.code == 'BTN_START':
                        global control_map
                        if control_map == "Easy":
                            control_map = "Advanced"
                        elif control_map == "Advanced":
                            control_map = "Easy"

                        print("Control mode: {}".format(control_map))

                response = remote.send(map_btn(event.code, event.state), port) # Send mapped input to CAM
                # TODO timeout for response

                if response != "OK":  # Not understood
                    if response == "CC":
                        print("Exiting manual control")
                        return
                    else:
                        print("Exiting manual control, error: {}".format(response))
                        return

        append(axis) # Update most recent values


# Begin and manage manual control mode
def init():
    logging.info("Starting manual control")

    time.sleep(2)  # Prevent race condition as CAM sets up for run

    # This all obeys GIL so there *shouldn't* be race conditions
    buffer = collections.deque(maxlen=1) # Buffer to hold most recent values

    # Start iterator
    it = threading.Thread(target=read_output, args=(buffer.append,))
    it.daemon = True
    it.start()

    # Get axis info regularly
    while True:
        time.sleep(.25)  # Don't overwhelm network (lowest possible is probably ~0.005 sec)

        if not it.is_alive(): # Iterator exited
            break

        try:
            response = remote.send(map_axis(buffer[0]), port) # Send mapped input to CAM
            # TODO timeout for response
        except:
            logging.warning("Controller input empty")
            response = "OK"

        if response != "OK":  # Not understood
            if response == "CC":
                print("Exiting manual control")
                break
            else:
                print("Error, exiting manual control")
                break



    print("Stopping CAM")
    remote.send("STOP", port) # Stop command


# Testing
if __name__ == "__main__":
    init()