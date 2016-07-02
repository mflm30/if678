#!usr/bin/env python

import socket
import threading
import select
import time
import netifaces # pegar o ip do cliente pae

#classe princiapal pae
def main():

    class cliente(threading.Thread):
            C_IP   = netifaces.ifaddresses('eth0')[2][0]['addr']
            C_PORT = 2345 #meia 78, ta na hora de molhar o biscoito
            PORT = 1776 #porta do servidor, a de cima e a do cliente

            def __init__(self):
                threading.Thread.__init__(self)
                self.host = '127.0.0.1' # localhost pae, ip do servidor e fixo
                self.sock = None #sei o que é isso não
                self.running = 1 #roda o loop da comunicação
                # enviando o IP para o servidor, e avisando que ta no ar
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    s.bind((HOST,PORT))
                except Exception, e:
                    print "Chorou :" +e
                else:
                    print "BIURR"
                finally:
                    s.listen(1) # é 13 porra, biur
                self.conn, self.addr = s.accept()
                conn.send(C_IP+"|"C_PORT) # enviando o IP|PORTA para o servidor
            def enviar(self):
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                e_host = 'localhost'
                e_port = 6000
                try:
                    conexao = (e_host,e_port)
                    tcp.bind (conexao)
                except socket.error as e:
                    print (e)
                    exit(0)
                # ctrl + v
                tcp.listen(1)
                conn, addr = tcp.accept()
                arquivo = open ('roberto-macho.jpg','rb')
                try:
                    pacote = arquivo.read(1024)
                    while pacote != '':
                        conn.send(pacote)
                        pacote = arquivo.read(1024)
                finally:
                    arquivo.close()
                    tcp.close()
                    conn.close()
            def recebe(self):
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                r_host = 'localhost'
                r_port = 6000
                conexao = (r_host,r_port)
                tcp.connect (conexao)
                # ctrl + v
                nome = "roberto.jpg"
                nomesaida = ("./" + nome)
                saida = open (nomesaida,'wb')
                data = tcp.recv(1024)
                while data != '':
                    saida.write(data)
                    data = tcp.recv(1024)
                # arquivorecebido = data.split('\n')
                # nome,tamanho=arquivorecebido[5].split(' ')
                # testezao.printlista()
                saida.close()
                tcp.close()
            def kill(self):
                self.running = 0

if __name__ == "__main__":
    main()
