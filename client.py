
import sys
from socket import *
import threading

def get_messages():
    while True:
        message = client_socket.recv(200)
        print(message.decode())
    return

SERVER_IP = "0.0.0.0"
SERVER_PORT = '12033'
if (len(sys.argv) < 3):
    print("Usage: python3 " + sys.argv[0] + " relay_port integer_to_send")
    sys.exit(1)
assert(len(sys.argv) == 3)
relay_port=int(sys.argv[1])

# Read integer
data=sys.argv[2]

# Create a socket for the sender
client_socket=socket(AF_INET, SOCK_STREAM)

#connect client to server
client_socket.connect((SERVER_IP, SERVER_PORT))

# send username to server
username = input("enter username")
client_socket.send(username.encode())

listen_thread = threading.Thread(target=get_messages, args=())
listen_thread.start()

while True:
    message = input()
    client_socket.send(message.encode())
