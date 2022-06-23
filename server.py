# -- coding: utf-8 --
""" -- python 3.10.4 -- """
import socket
import threading


class Server:
    def __init__(self, address='', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.sock.listen(10)
        self.list = []

    def accept(self):
        self.sock.listen(5)
        client, addr = self.sock.accept()
        self.threads = []
        print("Cliente conectado: ", addr)
        thread = threading.Thread(target=self.recvmsg, args=(client, addr))
        thread.start()

    def recvmsg(self, client, addr: tuple):
        self.decoded = ''
        while True:
            try:
                data = client.recv(1024)
                self.decoded = data.decode('utf-8')
                if not data:
                    break
            except Exception as e:
                print("Cliente desconectado addr: ", addr[1])
                break

            msg = self.decoded.split('|')
            if msg[0] == 'rec':
                client.sendall(bytes(self.prepareData(), "utf-8"))
            elif msg[0] == 'add':
                msg.pop(0)
                self.list.append(msg)
            elif msg[0] == 'mod':
                msg.pop(0)
                for i in self.list:
                    if(i[0] == msg[0]):
                        self.list.remove(i)
                        self.list.append(msg)
            elif msg[0] == 'del':
                for i in self.list:
                    if(i[0] == msg[1]):
                        self.list.remove(i)
        client.close()
        print("Cliente desconectado addr: ", addr[1])

    def format(self, text: str):
        return text.replace(',', '.')

    def prepareData(self):
        msg = str(len(self.list))
        for i in self.list:
            msg += '|' + i[0] + ',' + i[1] + ',' + i[2] + ','
            msg += self.format(str(i[3])) + ',' + i[4] + ','
            msg += self.format(str(i[5])) + ','
            msg += self.format(str(i[6])) + ','
            msg += self.format(str(i[7]))
        return msg

    def close(self):
        self.sock.close()


server = Server('127.0.0.1', 9090)

while True:
    server.accept()
