import socket

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
arquivo = open ('partiu.txt','rb')
try:
	pacote = arquivo.read(1024)
	print(pacote)
	conn.send(pacote)
finally:
	arquivo.close()
	tcp.close()
	conn.close()
