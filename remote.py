# Establish network connection to CAM/remote.py
# Acts as TCP/IP client

import socket

# Send data to CAM and return the response
def send(data, port):
    host = "127.0.0.1"  # TODO: Set to CAM's static IP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(bytes(data, 'utf-8'))
        response = s.recv(1024).decode('utf-8') # Buffer size
        return response

if __name__ == "__main__":
    print(send("STasdf", 6969)) # Test message