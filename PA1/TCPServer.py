# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Server
# Description: This is a simple TCP server socket which receives a message from
# the client and then converts the string to upper case letters and sends the 
# messag back to the client

import socket
HOST = socket.gethostname() 
PORT = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            modifiedMessage = data.decode().upper()
            conn.sendall(modifiedMessage.encode())