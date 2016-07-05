import socket
import threading
import time
 
# class Cliente(object):
#   def __init__(self,identificador,tabela):
#       self.identificador = identificador
#       self.tabela = tabela
 
 
class Servidor (threading.Thread):
        tabela = {}
        lock = threading.Lock()
        host = ''
        port = 5578
        conexao = (host,port)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            conexao = (host,port)
            tcp.bind (conexao)
        except socket.error as e:
            print (e)
            exit(0)
        tcp.listen(4)
       
 
        def __init__ (self):
            threading.Thread.__init__(self)
            self.conn = None
            self.addr = None
            self.threadAtiva = True
 
       
        def run(self):
           
            print("ESPERANDO")
            self.conn,self.addr = Servidor.tcp.accept()
            print("CONECTOU")          
            data = self.conn.recv(1024)
            data = eval(data)
            print (data)
            # self.lock.acquire()
            # Servidor.tabela[data.keys()[0]] = {}
            # Servidor.tabela[data.keys()[0]]['tem'] = data[data.keys()[0]]['tem']
            # Servidor.tabela[data.keys()[0]]['quero'] = data[data.keys()[0]]['quero']
            # print data.keys()[0][1]
            # self.lock.release()
            # print(Servidor.tabela)
           
 
 
            self.conn.close()
 
 
 
teste = Servidor()
teste.start()
teste2 = Servidor()
teste2.start()