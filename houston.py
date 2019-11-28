# Remote control program for the rover
import time
import logging
import remote
import manual
import autorun

logging.basicConfig(filename='houston.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.ERROR) # Log each run to file

port = 42069  # Port for network

# Tell CAM what to do
def houston(option):
    # Shutdown command
    if option.capitalize() == 'K':
        print("Sending shutdown command")
        print(remote.send('SD', port))

    # Self test
    elif option == '0':
        print("Running test")
        print(remote.send('ST', port))

    # Manual mode
    elif option == '1':
        print(remote.send('MM', port))
        manual.init()

    # Autonomous run
    elif option == '2':
        print(remote.send('AR', port))
        autorun.init()

    # Upload runfile to CAM
    elif option == '3':
        # TODO
        print(remote.send('UP', port))

# Main menu for running the robot
if __name__ == "__main__":
    # Wait until connected to CAM
    print("Connecting to CAM")
    ping = remote.send('HI', port)
    while ping == "Connection Error":
        print("Couldn't connect, retrying...")
        time.sleep(5)
        ping = remote.send('HI', port)
    print("Connected!")

    # Check status message
    if ping != 'HI':
        if ping == 'BZ': # Process is currently running
            ltk = input("Something is currently running; kill it? (Y/n)").capitalize()
            if ltk == "Y" or ltk == "":
                remote.send('KP', port)
            else:
                exit(0) # Bad stuff will probably happen unless we stop

    # Get user input
    while True:
        opt = input("Run Options:\n"
                    "\tQ - Exit Houston\n"
                    "\tK - Power down CAM\n"
                    "\tL - Retrieve logs from CAM\n"
                    "\t0 - Run self test\n"
                    "\t1 - Manual mode\n"
                    "\t2 - Run autonomous program\n"
                    "\t3 - Send autonomous program\n"
                    "Enter choice: ")
        if opt.capitalize() == 'Q':
            exit(0)
        elif opt != '':
            houston(opt)