import socket
import threading
import time

class Servidor (threading.Thread):
	tabela = {}
	identificador = ()
	tabela[identificador] = {}
	tabela[identificador]['tem'] = []
	tabela[identificador]['quero'] = []
	host = ''
	port = 5599
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

	# deletar peer do dicionário
	def delete_peers(lista_de_peers, hostname):
	    lista_de_peers[:] = [d for d in lista_de_peers if d.get('Hostname') != hostname]
	    return lista_de_peers

	# P2S response message from the server
	def p2s_lookup_response(rfc_num): # the parameter "rfc_num" should be str
	    current_time = time.strftime("%a, %d %b %Y %X %Z", time.localtime())
	    response = search_combined_dict(rfc_num)
	    if not response:
	        status = "404"
	        phrase = "Not Found"
	        message= "P2P-CI1111/1.0 "+ status + " "+ phrase + "\n"\
	                 "Date: " + current_time + "\n"
	        return response, message
	    else:
	        status = "200"
	        phrase = "OK"
	        message	= "P2P-CI11111/1.0 "+ status + " "+ phrase + "\n"
	        return response, message

		def run(self):
			print("ESPERANDO")
			self.conn,self.addr = Servidor.tcp.accept()
			print("CONECTOU")
			data = self.conn.recv(1024)
			while data != '':
				data += self.conn.recv(1024)
			data = eval(data)
			Servidor.tabela[data.keys[0]]['tem'] = data[data.keys[0]]['tem']
			Servidor.tabela[data.keys[0]]['quer'] = data[data.keys[0]]['quer']


			self.conn.close()



teste = Servidor()
teste.start()
teste2 = Servidor()
teste2.start()
