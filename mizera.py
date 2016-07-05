#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading
import time
import fcntl
import struct
import os
import math

class Ping(object):
    def __init__(self,identificador,quero,tenho):
        self.identificador = identificador
        self.quero = quero
        self.tenho = tenho

class Arquivo(object):
    def __init__ (self,nome,tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.npacotes = int(math.ceil(float(tamanho)/1024)) #tamanho do pacote = 1024bytes = 1KB
        self.arquivo = [0 for i in range(self.npacotes)]

    def printlista(self):
        print self.nome
        print self.tamanho
        print self.npacotes
        print len(self.arquivo)

    def inserir(self,indice,data):
        self.arquivo[indice] = data

    def montar(self):
        nomesaida = ("./" + self.nome)
        saida = open(nomesaida,'wb')
        for i in self.arquivo: saida.write(i)
        saida.close()

class Cliente(object):
    def __init__(self,identificador ):
        self.identificador = identificador
        self.status = "Online"
        self.nomeconcluidos = []
        self.arquivosconcluidos = [[]]
        self.nomefaltantes = []
        self.arquivosfaltantes = [[]]
        self.ipsdonos = [[]]

    def arquivosiniciais(self,tenho,quero):
        self.nomeconcluidos = tenho
        for i in range(len(tenho)):
            self.arquivosconcluidos[i] = [1 for j in range(int(math.ceil(float(os.path.getsize(tenho[i]))/1024)))]
        for i in range(len(quero)):
            self.nomefaltantes.append(quero[i][0])
            self.arquivosfaltantes = [0 for j in range(int(math.ceil(float(quero[i][1])/1024)))]
            self.ipsdonos = [0 for j in range(int(math.ceil(float(quero[i][1])/1024)))]
    def printclient(self):
        print(self.identificador) 
        print (self.status)
        print (self.nomeconcluidos) 
        print (self.arquivosconcluidos)
        print (self.nomefaltantes)
        print (self.arquivosfaltantes)
        print (self.ipsdonos)



class Arquivo(object):
    def __init__(self,nome,tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.npacotes = int(math.ceil(float(tamanho)/1024)) #tamanho do pacote = 1024bytes = 1KB
        self.arquivo = [0 for i in range(self.npacotes)]
        self.completude = verificarcompletude(self)

    def printlista(self):
        print self.nome
        print self.tamanho
        print self.npacotes
        print len(self.arquivo)

    def inserir(self,indice,data):
        self.arquivo[indice] = data

    def montar(self):
        nomesaida = ("./" + self.nome)
        saida = open(nomesaida,'wb')
        for i in self.arquivo: saida.write(i)
        saida.close()

    def verificarcompletude(self):
        for i in self.arquivo:
            if i == 0:
                return False
        self.completude = True
        return True

#class Cliente(threading.Thread):

#FUNÇÃO PARA PEGAR O IP DO CLIENTE
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
#----------------------------------------------
#PARTE DO CODIGO SO PARA LER O ARQUIVO DE ENTRADA E ADD EM SERVIDOR(HOST,PORT) , TENHO[] , QUERO[(NOME,TAMANHO)]
arquivo = open('entrada.txt', "r")
servidor = (str(arquivo.readline()).replace("\n",''),int(str(arquivo.readline()).replace("\n",'')))
tenho = arquivo.readlines()
quero = []
asterisco = False
contarDels = 1
for i in range(len(tenho)):
    tenho[i] = str(tenho[i]).replace("\n",'')
    if asterisco == True:
        quero += [tenho[i]]
        contarDels += 1
    if tenho[i]=="*":
        asterisco = True
for i in range(contarDels):
    tenho.pop(len(tenho)-1)
for i in range(len(quero)):
    auxiliar = quero[i].split(' ')
    quero[i] = tuple(auxiliar)
print tenho, quero
arquivo.close()
#-----------------------------------------------
#FAZ CONEXÃO TCP COM O SERVIDOR
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = servidor[0]
port = servidor[1]
conexao = (host,port)
tcp.connect(conexao)


#----------------------------------------------
#DECLARANDO DICIONARIO QUE ARMAZENA AS INFORMAÇÕES DO CLIENTES
tabela = {}
identificador = (get_ip_address('eth0'),5000)
tabela[identificador] = {}
tabela[identificador]['tem'] = tenho
tabela[identificador]['quero'] = quero

cliente = Cliente(identificador)
cliente.arquivosiniciais(tenho,quero)
cliente.printclient()

#-----------------------------------------------
tcp.send(str(tabela))

tcp.close()
