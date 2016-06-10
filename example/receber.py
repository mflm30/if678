import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000
conexao = (host,port)
tcp.connect (conexao)

saida = open ('./saida','wb')

data = tcp.recv(1024)
hostcliente,portcliente,restante = data.split('\n',2)
print(hostcliente)
print(portcliente)
#print(restante)

tcp.close()
saida.close()

