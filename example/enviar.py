import socket
import threading
import select
import time

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000
try:
	conexao = (host,port)
  	tcp.bind (conexao)
except socket.error as e:
	print (e)
  	exit(0)


tcp.listen(1)
conn, addr = tcp.accept()
arquivo = open ('partiu.txt','rb')
try:
	pacote = arquivo.read(1024)
	print(pacote)
	conn.send(pacote)
finally:
	arquivo.close()
	tcp.close()
	conn.close()

def main():
	# Servidor (que enviar o arquivo)
    class Server(threading.Thread):
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
                s.listen(1)
                self.conn, self.addr = s.accept()
                # Select loop for listen
                while self.running == True:
                    inputready,outputready,exceptready \
                      = select.select ([self.conn],[self.conn],[])
                    for input_item in inputready:
                        # Handle sockets
                        data = self.conn.recv(1024)
                        if data:
                            print "Them: " + data
                        else:
                            break
                    time.sleep(0)
            def kill(self):
                self.running = 0
     # Cliente (receber o arquivo )
    class Client(threading.Thread):
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
                    for input_item in inputready:
                        # Handle sockets
                        data = self.sock.recv(1024)
                        if data:
                            print "Them: " + data
                        else:
                            break
                    time.sleep(0)
            def kill(self):
                self.running = 0
    # entrada de dados
    class data_Input(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.running = 1
            def run(self):
                while self.running == True:
                  text = raw_input('')
                  try:
                      client.sock.sendall(text)
                  except:
                      Exception
                  try:
                      server.conn.sendall(text)
                  except:
                      Exception
                  time.sleep(0)
            def kill(self):
                self.running = 0

    # Prompt, object instantiation, and threads start here.

    ip_addr = raw_input('What IP (or type listen)?: ')

    if ip_addr == 'listen':
        server = Server()
        client = Client()
        server.start()
        text_input = Text_Input()
        text_input.start()
        
    elif ip_addr == 'Listen':
        server = Server()
        client = Client()
        server.start()
        text_input = Text_Input()
        text_input.start()
        
    else:
        server = Server()
        client = Client()
        client.host = ip_addr
        text_input = Text_Input()
        chat_client.start()
        text_input.start()

if __name__ == "__main__":
    main()