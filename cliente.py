import socket
import threading
import time

arquivo = open('entrada.txt', "r")


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

#PARTE DO CODIGO SO PARA LER O ARQUIVO DE ENTRADA E ADD EM SERVIDOR(HOST,PORT) , QUERO[] , TENHO[(NOME,TAMANHO)]
servidor = (str(arquivo.readline()).replace("\n",''),str(arquivo.readline()).replace("\n",''))
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
arquivo.close()
#-----------------------------------------------
