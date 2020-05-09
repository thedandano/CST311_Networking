# Name: Dan Sedano
# Date: 05/04/2020
# Title: UDP Server
# Description: This is a simple UDP server socket which receives a message from
# the client and then converts the string to upper case letters and sends the 
# messag back to the client

from socket import *
serverPort = 12000
# Instantiates the socket object with IPv4 and the UDP protocol.
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assigns the port number to the server socket
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
# While loop allows for indefinite processing of messages from client.
while True:
    # Receives UDP messages. recvfrom() returns a pair message and the client's address
    # (message, (IP, port #)). 
    message, clientAddress = serverSocket.recvfrom(2048)
    # Decodes the message (Byte to String). Then processes the string message to upper case letters
    modifiedMessage = message.decode().upper()
    # Encodes the message first (String to Byte). 
    # Then returns the message to the client using the previously received address.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
