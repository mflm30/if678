import socket
import math

class Arquivo(object):
	def __init__ (self,nome,tamanho):
		self.nome = nome
		self.tamanho = tamanho
		self.npacotes = int(math.ceil(float(tamanho)/1024)) #tamanho do pacote = 1024bytes = 1KB
		self.arquivo = []

	def printlista(self):
		print self.nome
		print self.tamanho
		print self.npacotes
		print self.arquivo

	def inserir(self):
		pass




tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000
conexao = (host,port)
tcp.connect (conexao)

nome = "roberto.jpg"
nomesaida = ("./" + nome)
saida = open (nomesaida,'wb')
while tcp.recv(1024)!='':
	data = tcp.recv(1024)
	testezao = Arquivo(nome,1079915)
	saida.write(data)
# arquivorecebido = data.split('\n')
# nome,tamanho=arquivorecebido[5].split(' ')

# testezao.printlista()

saida.close()
tcp.close()