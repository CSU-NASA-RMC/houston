# Remote control program for the rover
import time
import logging
import remote
import manual
import autorun

port = 42069  # Carefully chosen

# Tell CAM what to do
def houston(option):
    # TODO: Responses may need timeout fails

    # Shutdown command
    if option.capitalize() == 'K':
        print("Sending shutdown command")
        print(remote.send('SD', port))

    # Self test
    elif option == '0':
        print("Running test")
        st_result = remote.send('ST', port)
        print(st_result)
        if st_result != 'PASS':
            want_cont = input("Proceed? (y/N): ")
            if want_cont.capitalize() != 'Y':
                exit(1)

    # Manual mode
    elif option == '1':
        print(remote.send('MM', port))
        manual.init()

    # Autonomous run
    elif option == '2':
        print(remote.send('AR', port))
        autorun.init()

    elif option == '3':
        print("Not yet implemented")

def ping_CAM():
    try:
        return remote.send('HI', port)
    except:
        return "can't connect"

if __name__ == "__main__":
    # Ping to see if CAM is running
    print("Connecting to CAM")
    while ping_CAM() != 'HI':
        print("Couldn't connect, retrying...")
        time.sleep(5)
    print("Connected!")
    while True:
        opt = input("Run Options:\n"
                    "\tQ - Exit Houston\n"
                    "\tK - Power down CAM\n"
                    "\t0 - Run self test\n"
                    "\t1 - Manual mode\n"
                    "\t2 - Run autonomous program\n"
                    "\t3 - Send autonomous program\n"
                    "Enter choice: ")
        if opt.capitalize() == 'Q':
            exit(0)
        elif opt != '':
            houston(opt)