# -- coding: utf-8 --
""" -- python 3.10.4 -- """
import socket


class Socket:
    def __init__(self, address='', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.saved_data = ''

    def recvmsg(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('Conectado a :', self.addr)
        self.decoded_data = ''

        while True:
            data = self.conn.recv(10000)
            self.decoded_data += data.decode("utf-8")
            if not data:
                break

            # Se for um receiver envia os dados para o cliente
            if(self.decoded_data.find('receiver') != -1):
                self.conn.send(bytes(self.saved_data, "utf-8"))
                print("Enviado para receiver: " + self.saved_data)
            else:
                # Se for o master salva os dados do cliente
                self.saved_data = self.decoded_data
                self.conn.send(bytes("ok salvo", "utf-8"))
                print("Salvo do master: " + self.saved_data)

            self.conn.close()
            return self.decoded_data

    def close(self):
        self.sock.close()


server = Socket('127.0.0.1', 9090)

while True:
    msg = server.recvmsg()
