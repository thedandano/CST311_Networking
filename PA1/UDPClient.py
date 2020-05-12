# Name: Dan Sedano
# Date: 05/04/2020
# Title: UDP Client
# Description: This is a simple UDP client Socket which sends a lower case string to the 
# server client and receives a response and then decodes the response.

from socket import *
# gets the host's IP. In this case host is also destination
serverName = gethostbyname(gethostname()) 
serverPort = 12000

# Instantiates the socket object with AF_INET (IPv4) and SOCK_DGRAM (UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Input lowercase sentence: ')
# Encodes the message to Byte type and Transmits the message via UDP using the 
# server's address information. 
clientSocket.sendto(message.encode(),(serverName, serverPort))
# Receives UDP messages. recvfrom() returns a pair, the modified message
# from the server and teh server address (string, (IP, Port #)).
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# Decodes the message (Byte to String) and prints out to console.
print(modifiedMessage.decode())
# Closes the socket connection
clientSocket.close()
