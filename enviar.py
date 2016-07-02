import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = 'localhost'
port = 4587
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
	conn.send("0")
	pacote = arquivo.read(1024)
	while pacote != '':
		conn.send(pacote)
		pacote = arquivo.read(1024)
finally:
	arquivo.close()
	conn.close()
	tcp.close()
