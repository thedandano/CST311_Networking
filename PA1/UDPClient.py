from socket import *
serverName = 'hostname'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(servierName, serverPort))
modifiedMessage, serverAddress = clientSocket.rcvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
