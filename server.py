
import sys
from socket import *
import threading

def communication(other_ip, other_port, other_socket, client_username, clients_list, clients_dict):
    while True:
        # receive data
        data = other_socket.recv(200)
        message = data.decode()
        # check if sender has ended connection
        if (message == ""):
            print(f"Client {other_ip}, {other_port} has disconnected")
            clients_list.remove(other_socket)
            clients_dict.pop()
            break
        words = message.split()
        # if addressed to a username using @
        if (words[0][0] == '@'):
            # send message only to username being @ed
            feature2(message, clients_dict, other_socket)
        # if no @
        else:
            # broadcast message to everybody
            feature1(message, other_ip, other_port, clients_list, other_socket)


def feature2(message, clients_dict, client_socket):
    #feature 2 here
    return

def feature1(message, sender_ip, sender_port, clients_list, client_socket):
    #feature 1 here
    for client in clients_list:
        if client != client_socket:
            client.send(message.encode())
    
    return

HOST = '0.0.0.0' 
PORT = '12033'


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(1)
clients_dict = {} # maps username and socket
clients_list = []
threads_list = []
while True:
    
    client_socket, client_address = server_socket.accept()
    clients_list.append(client_socket)
    
    # Get client's username for feature 2
    client_username = "placeholder"
    clients_dict[client_username] = client_socket
    # add username, address pair to dict

    # make thread to handle client
    client_thread = threading.Thread(target = communication, args = (client_address[0], client_address[1], client_socket, client_username, clients_list, clients_dict))
    threads_list.append(client_thread)
    client_thread.start()

# Close any open sockets
server_socket.close()
