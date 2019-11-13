# Establish network connection to CAM/remote.py
# Acts as TCP/IP client

import socket

# Send data to CAM and return the response
# Input and output are byte objects
def send(data):
    host = "127.0.0.1"  # TODO: Set to CAM's static IP
    port = 42069  # Carefully chosen

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
        return s.recv(1024) # Buffer size

if __name__ == "__main__":
    print(send(b"ST")) # Test message