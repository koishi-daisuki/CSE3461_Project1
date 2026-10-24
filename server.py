
import sys
from socket import *
import threading

# function for receiving and sending message from each client
def communication(other_ip, other_port, other_socket, clients_list, clients_dict):
    # username should be first thing sent by client
    # add username, socket pair to dictionary
    data = other_socket.recv(200)
    username = data.decode()
    clients_dict[username] = other_socket
    try:
        while True:
            # receive data
            data = other_socket.recv(200)
            message = data.decode()
            # check if sender has ended connection
            if (message == ""):
                print(f"Client {other_ip}, {other_port} has disconnected")
                # remove client from lists
                clients_list.remove(other_socket)
                clients_dict.pop()
                break
            # add an identifying username to each message
            final_message = f"{username}: {message}"
            words = message.split()
            # if addressed to a username using @
            if (words[0][0] == '@'):
                # send message only to username being @ed
                feature2(final_message, clients_dict, other_socket)
            # if no @
            else:
                # broadcast message to everybody
                feature1(final_message, other_ip, other_port, clients_list, other_socket)
    except KeyboardInterrupt:
        return

def feature2(message, clients_dict, client_socket):
    #TODO: feature 2 here
    return

def feature1(message, sender_ip, sender_port, clients_list, client_socket):
    #feature 1 here
    # send to every client except sender
    for client in clients_list:
        if client != client_socket:
            client.send(message.encode())
    
    return

#host and port
#TODO: implement simulation vs over-the-air mode
HOST = '0.0.0.0' 
PORT = 12033
# create socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST,PORT))
# listen for connection requests
server_socket.listen(1)
clients_dict = {} # maps username and socket
clients_list = [] # list of client sockets
threads_list = [] # list of client threads
try:
    while True:
        # accept connection
        client_socket, client_address = server_socket.accept()
        # add to list
        clients_list.append(client_socket)

        # make thread to handle client
        client_thread = threading.Thread(target = communication, args = (client_address[0], client_address[1], client_socket, clients_list, clients_dict))
        threads_list.append(client_thread)
        client_thread.start()
except KeyboardInterrupt:
    # Close any open sockets
    server_socket.close()
