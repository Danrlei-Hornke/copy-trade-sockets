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

# adicionar um ordem ao servidor
# add|id_da_ordem|sentido|ativo|entrada|data|quantidade|perda|ganho
msg = client.sendData("add|12345|BUY|EURUSD|1.10000|01/01/2022 00:00:00|0.01|1.05000|1.15000")
# atualizar uma ordem no servidor 
# mod|id_da_ordem|sentido|ativo|entrada|data|quantidade|perda|ganho
msg = client.sendData("mod|12345|BUY|EURUSD|1.10000|01/01/2022 00:00:00|0.01|1.00000|1.20000")
# excluir uma ordem no servidor parâmetro 
# del|id_da_ordem
msg = client.sendData("del|12345")
client.showData()
