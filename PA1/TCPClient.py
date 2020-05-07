# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Client
# Description: This is a simple TCP client Socket which sends a lower case string to the 
# server client and receives a response and then decodes the response.


# import socket
# HOST = socket.gethostname()
# PORT = 1024

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     message = input('Input lowercase sentence: ')
#     s.sendall(message.encode())
#     msg=s.recv(1024)
#     print(msg.decode("utf-8"))
#     s.close()

from socket import *
serverName = gethostname()
serverPort = 12000
# creates socket object with IPv4 Protocol (AF_INET) TCP Protocol (Sock_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)
# establishes connection
clientSocket.connect((serverName, serverPort))
# asks for user input
sentence = raw_input('Input lowercase sentence: ')
# encodes the user input and transmits to server socket
clientSocket.send(sentence.encode())
# receives encoded returned response from server
modifiedSentence = clientSocket.recv(1024)
# decodes modifiedSentence and prints out to terminal
print('From Server: ' + modifiedSentence.decode())
# closes the socket
clientSocket.close()
