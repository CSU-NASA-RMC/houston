# Establish network connection to CAM/remote.py
# Acts as TCP/IP server

import socket
from termcolor import colored

# Set a function to receive data from CAM and sends the return
def listen(operation):
    host = '' # All network interfaces
    port = 42069 # Unused port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            #print("Connected to CAM ", addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                #print(colored(str(data), 'grey', 'on_white'))
                response = operation(data)
                conn.sendall(response)
                return response
    return