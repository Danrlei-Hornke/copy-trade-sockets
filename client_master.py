# -- coding: utf-8 --
""" -- python 3.10.4 -- """

import socket


class Client:
    def __init__(self, address='', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.data = ''

    def sendData(self, data):
        self.sock.connect((self.address, self.port))
        self.sock.sendall(bytes(data, "utf-8"))
        self.data = self.sock.recv(1024).decode("utf-8")
        self.sock.close()
        return self.data

    def showData(self):
        print("Recebido :", self.data)


# Criar um cliente
client = Client("127.0.0.1", 9090)

""" Resposta que o servidor vai fornecer sobre o salvamento dos dados."""
msg = client.sendData("open:10,close:20,high:30,low:40,volume:50")
client.showData()
