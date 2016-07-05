import socket
import threading
import time

class puta(object):
	""" Classe principal para o cliente.
		@__init__: Inicia e cria uma conexão com o servidor,
		enviar todas as informações para o serve.
		@p2p_get: faz uma requisição direto a outro peer, para 
		download de algum arquivo."""
	def __init__(self):
		upload_port_num = 65000+random.randint(1, 500)  # gerar uma porta aleatória entre 65000~65500
		dicionario_list = []  # lista de RFCs e titulos dos arquivos pae.
		s=socket.socket() 
		#s.setsockopt(socket.SOL_SOCKET, socket.SO_RESUEDADDR, 1)
		#host = socket.gethostname()  # isso não ta funcionando pae
		host = "127.0.0.1"       # ip do servidor
		port = 7734              # porta reservada para o serviço
		s.connect((host, port))
		data = pickle.dumps(peer_informacoes())  # enviar todas as informações para o servidor
		s.send(data)
		data = s.recv(1024)
		print(data.decode('utf-8')) # to usando esse decode, e importante pae... se o arquivo tiver caracteres especiais da treta.
		s.close

	# Fazer requisição de arquivo a um peer
	# rfc_num = numero ou hash do arquivo
	# peer_host = host, peer_upload_port = porta né pae
	def p2p_get(rfc_num, peer_host, peer_upload_port):
	    s = socket.socket()
	    s.connect((peer_host, int(peer_upload_port)))
	    data = ''
	    s.send(bytes(data, 'utf-8'))
	    data_rec = pickle.loads(s.recv(1024))
	    print("Data_rec", str(data_rec))
	    #my_data = data_rec.decode('utf-8')
	    my_data = data_rec[1]
	    print(my_data)
	    current_path = os.getcwd()
	    filename = "rfc"+rfc_num+".txt"
	    #f = open(filename,'w')
	    with open(filename, 'w') as file:
	        file.write(my_data)
	    #f.write(data_rec.decode('utf-8'))
	    #f.close()
	    s.close()

	# Informações do peer
	# retorna uma tudos os arquivos que tem localmente
	def peer_informacoes():
	    keys = ["RFC Number", "RFC Title"]
	    rfcs_num = get_local_rfcs()
	    rfcs_title = get_local_rfcs()  # ["title1", "title2", "title3"] we use rfcs_num to fill in title
	    for num, title in zip(rfcs_num, rfcs_title):
	        entry = [num, title]
	        dict_list_of_rfcs.insert(0, dict(zip(keys, entry)))
	    return [upload_port_num, dict_list_of_rfcs]  # [port, rfcs_num, rfcs_title]

arquivo = open('entrada.txt', "r")

class Ping(object):
	def __init__(self,identificador,quero,tenho):
		self.identificador = identificador
		self.quero = quero
		self.tenho = tenho

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
