# Establish network connection to CAM/remote.py
# Acts as TCP/IP client

import socket
import time

# Send data to CAM and return the response
# Input and output are byte objects
def send(data, port):
    host = "127.0.0.1"  # TODO: Set to CAM's static IP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(bytes(data, 'utf-8'))
        return s.recv(1024).decode('utf-8') # Buffer size


def send_until(data, port, tries):
    for i in range(tries):
        try:
            rec = send(data, port)
            return rec
        except:
            print("Failed to send ({}/{})".format(i, tries))
            time.sleep(1)
    return ""

if __name__ == "__main__":
    print(send("STasdf", 6969)) # Test message