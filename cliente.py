import socket
import threading
import time

arquivo = open('entrada.txt', "r")


class Ping(object):
	def __init__(self,identificador,quero,tenho):
		self.identificador = identificador
		self.quero = quero
		self.tenho = tenho

identificador = (str(arquivo.readline()).replace("\n",''),str(arquivo.readline()).replace("\n",''))
#while arquivo.readline() != "*\n":
tenho = []
quero = []
for i in arquivo.readlines():
	if (i != '*\n'):
		tenho += [i.replace("\n",'')]
	else:
		quero = [i.replace("\n",'')]
print tenho
print quero