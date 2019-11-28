# Establish network connection to CAM/remote.py
# Acts as TCP/IP client

import socket
import logging

# TODO: Timeout failure

# Send data to CAM and return the response
def send_unsafe(data, port):
    host = "192.168.1.102"  # TODO: Set to CAM's static IP
    logging.debug("Sending on port {}: {}".format(port, data))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Data is encoded for TX/RX
        s.sendall(bytes(data, 'utf-8'))
        response = s.recv(1024).decode('utf-8') # Buffer size

        logging.debug("Received on port {}: {}".format(port, response))
        return response

# Throws errors when host is not up yet
def send(data, port):
    try:
        return send_unsafe(data, port)
    except:
        logging.error("Network error")
        return "Connection Error"

# Testing
if __name__ == "__main__":
    print(send("ST", 6969))
