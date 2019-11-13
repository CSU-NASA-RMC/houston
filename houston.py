# Remote control program for the rover
import time
import remote
import manual
import autorun

# Tell CAM what to do
def houston(option):
    # TODO: Responses may need timeout fails

    # Shutdown command
    if option.capitalize() == 'K':
        print("Sending shutdown command")
        print(remote.send(b'SD'))

    # Self test
    elif option == '0':
        print("Running test")
        st_result = remote.send(b'ST')
        print(st_result)
        if st_result != b'PASS':
            want_cont = input("Proceed? (y/N): ")
            if want_cont.capitalize() != 'Y':
                exit(1)

    # Manual mode
    elif option == '1':
        print("Starting manual mode")
        print(remote.send(b'MM'))
        manual.init()

    # Autonomous run
    elif option == '2':
        print("Setting up autonomous run")
        print(remote.send(b'AR'))

def ping_CAM():
    try:
        return remote.send(b'HI')
    except:
        return "can't connect"

if __name__ == "__main__":
    # Ping to see if CAM is running
    print("Connecting to CAM")
    while ping_CAM() != b'HI':
        print("Couldn't connect, retrying...")
        time.sleep(5)
    print("Connected!")
    while True:
        opt = input("\n### Run Options ###\n\n"
                    "Q - Exit Houston\n"
                    "K - Power down CAM\n"
                    "0 - Run self test\n"
                    "1 - Enable manual mode\n"
                    "2 - Run autonomous program\n"
                    "\nEnter choice: ")
        if opt.capitalize() == 'Q':
            exit(0)
        elif opt != '':
            print("Running option: ", opt)
            houston(opt)