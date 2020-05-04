# Name: Dan Sedano
# Date: 05/04/2020
# Title: UDP Server
# Description: This is a simple UDP server socket which receives a message from
# the client and then converts the string to upper case letters and sends the 
# messag back to the client

from socket import *

serverPort = 12000
# instantiates the socket object with IPv4 and the UDP protocol.
serverSocket = socket(AF_INET, SOCK_DGRAM)
# assigns the portnumber
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    # Receives UDP messages. recvfrom() returns a pair (string, address)
    message, clientAddress = serverSocket.recvfrom(2048)
    # converts the string message to upper case letters
    modifiedMessage = message.decode().upper()
    # returns the message to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
