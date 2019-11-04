# Remote control program for the rover
from termcolor import colored
import remote
import manual_xb

def houston(opt):
    opt = int(opt)
    if opt == 0:
        manual_xb.init()

# Wait for CAM to connect
def connect(data):
    return b"OK"

# Evaluate self check
def boot(data):
    if data == b"PASS":
        print("Self checks PASS!")
        return bytes(input("Enter operating mode: "), 'utf-8')
    else:
        print("Self checks FAIL!")
        print(colored(str(data), 'grey', 'on_white'))
        if input("Continue (y/n)?") == "y":
            return bytes(input("Enter operating mode: "), 'utf-8')
        else:
            return b"-1"

if __name__ == "__main__":
    print("Waiting for CAM to connect")
    remote.listen(connect)
    print("Waiting for CAM to boot")
    houston(remote.listen(boot))
    input("Press enter to close")