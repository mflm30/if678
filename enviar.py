import socket
# import threading

# class ClientThread(threading.Thread):

#     def __init__(self,ip,port):
#         threading.Thread.__init__(self)
# 		self.ip = ip
# 		self.port = port
#         print "[+] New thread started for "+ip+":"+str(port)


#     def run(self):    
#         print "Connection from : "+ip+":"+str(port)

#         clientsock.send("\nWelcome to the server\n\n")

#         data = "dummydata"

#         while len(data):
#             data = clientsock.recv(2048)
#             print "Client sent : "+data
#             clientsock.send("You sent me : "+data)

#         print "Client disconnected..."

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
