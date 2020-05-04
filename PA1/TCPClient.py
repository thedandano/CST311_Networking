# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Client
# Description: This is a simple TCP client Socket which sends a lower case string to the 
# server client and receives a response and then decodes the response.


import socket
HOST = socket.gethostname()
PORT = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input('Input lowercase sentence: ')
    s.sendall(message.encode())
    msg=s.recv(1024)
    print(msg.decode("utf-8"))
    s.close()
