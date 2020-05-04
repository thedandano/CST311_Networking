# Name: Dan Sedano
# Date: 05/04/2020
# Title: UDP Client
# Description: This is a simple UDP client Socket which sends a lower case string to the 
# server client and receives a response and then decodes the response.

from socket import *
serverName = gethostname() # gets the host's name
serverPort = 12000

#instantiates the socket object with AF_INET (IPv4) and SOCK_DGRAM (UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Input lowercase sentence: ')
# Transmits UDP messages
clientSocket.sendto(message.encode(),(serverName, serverPort))
# Receives UDP messages. recvfrom() returns a pair (string, address)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
# closes the socket connection
clientSocket.close()
