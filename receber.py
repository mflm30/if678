import socket
import math

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


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = 'localhost'
port = 4587
conexao = (host,port)
tcp.connect (conexao)

#saida = open (nomesaida,'wb')
nome = "roberto-saida.jpg"
arquivo = Arquivo(nome,1079915)

indice = int(tcp.recv(1024))
data = tcp.recv(1024)
while data != '':
	arquivo.inserir(indice,data)
#	saida.write(data)
	data = tcp.recv(1024)
	indice+=1
arquivo.montar()
# arquivorecebido = data.split('\n')
# nome,tamanho=arquivorecebido[5].split(' ')
arquivo.printlista()
tcp.close()
