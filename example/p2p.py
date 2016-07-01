#!usr/bin/env python

import socket
import threading
import select
import time

#classe princiapal pae
def main():

    class Server(threading.Thread):
            # propriedados
            clientes = [];

            # metodos
            def __init__(self):
                threading.Thread.__init__(self)
                self.running = 1
                self.conn = None
                self.addr = None
            def run(self):
                HOST = ''
                PORT = 1776
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST,PORT))
                s.listen(13) # é 13 porra
                self.conn, self.addr = s.accept()
                # Select loop for listen
                while self.running == True:
                    inputready,outputready,exceptready \
                      = select.select ([self.conn],[self.conn],[])
                    for input_item in inputready:
                        # Handle sockets
                        data = self.conn.recv(1024)
                        if data:
                            clientes.append(data) # adicionando um cliente na lista
                        else:
                            break
                    # não sei para que serve esse sleep
                    time.sleep(0)
            def kill(self):
                self.running = 0
     
    class cliente(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.host = None
                self.sock = None
                self.running = 1
            def run(self):
                PORT = 1776
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, PORT))
                # Select loop for listen
                while self.running == True:
                    inputready,outputready,exceptready \
                      = select.select ([self.sock],[self.sock],[])
                    # pegando o arquivo pae
                    arq = open('foo.tar.gz', 'w')
                    # enviando em pacotes pae
                    while 1:
                        dados = conn.recv(1024)
                        if not dados:
                            break
                        arq.write(dados)
                    # fechando o arquivo pae
                    arq.close()
                    time.sleep(0)
            def send(self):
                HOST = ''
                PORT = 1776
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST,PORT))
                s.listen(13) # é 13 porra
                self.conn, self.addr = s.accept()
                # Select loop for listen
                while self.running == True:
                    inputready,outputready,exceptready \
                      = select.select ([self.conn],[self.conn],[])
                    # pegando o arquivo pae
                    arq = open('financeiro.tar.gz', 'r')
                    # enviando em pacotes pae
                    for i in arq.readlines():
                        s.send(i)
                    # fechando o arquivo pae
                    arq.close()
                    # não sei para que serve esse sleep
                    time.sleep(0)
            def kill(self):
                self.running = 0
                
    class arquivo(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.running = 1
            def run(self):
                while self.running == True:
                  text = raw_input('')
                  try:
                      chat_client.sock.sendall(text)
                  except:
                      Exception
                  try:
                      chat_server.conn.sendall(text)
                  except:
                      Exception
                  time.sleep(0)
            def kill(self):
                self.running = 0
    # ex 

if __name__ == "__main__":
    main()
