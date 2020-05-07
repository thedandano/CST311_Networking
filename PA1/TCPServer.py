# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Server
# Description: This is a simple TCP server socket which receives a message from
# the client and then converts the string to upper case letters and sends the 
# messag back to the client

# import socket
# HOST = socket.gethostname() 
# PORT = 1024


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST,PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             modifiedMessage = data.decode().upper()
#             conn.sendall(modifiedMessage.encode())

from socket import *

serverPort = 12000

# creates socket object with IPv4 Protocol (AF_INET) TCP Protocol (Sock_STREAM)
serverSocket = socket (AF_INET, SOCK_STREAM)
# assigns a port number to the socket and does not assign an IP address.
# Therefore, any client that sends a message to this port will be accepted.
serverSocket.bind(('', serverPort))
# makes the socket ready to accept a connections. 
# The parameter (1) specifies the max queue of connections.
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # returns a connection socket object and the address of the bound socket from the client.
    connectionSocket, add = serverSocket.accept()
    # receives the message from the client and decodes the message
    sentence = connectionSocket.recv(1024).decode()
    # processes the message
    capitalizedSentence = sentence.upper()
    # encodes the message and then sends back to client
    connectionSocket.send(capitalizedSentence.encode())
    # closes the connection
    connectionSocket.close()