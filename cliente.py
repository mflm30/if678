import socket
import thread
import time

#define
pktLen = 5 # tamanho do pacote
timeout = 1 # timeout para enviar ping ao servidor
status = 1 # menu: imprimir informacoes
sair = 2 # sair do menu

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome = raw_input("Digite o nome do arquivo de entrada: ")
file = open(nome, 'r')

# conecta com o servidor
host = file.readline()
port = int(file.readline())

try:
    s.connect ( (host,port) )

except socket.error as e:
    print(e)
    exit(1)
#-----------------------------------
# funcao que dado um tamnho de arquivo(bytes), retorna aquantida de pacotes
def qtdPkt(tam):
    return ((tam-1)/pktLen+1)
#-------------------------------------
# inicializa vetores dos meus arquivos
meu = file.readline()
qtdTotal = 0
while (meu != ''):
    qtdTotal = qtdTotal + 1
    meu = file.readline()

qtdTotal = qtdTotal - 1

mineName = qtdTotal * ['']
mineLen = qtdTotal * [0]
mineMask = qtdTotal * [[1]]
file.close()
file = open(nome, 'r')
file.readline()
file.readline()
#----------------------------------------

# le quais arquivos tenho
meu = file.readline()
mineQtd = 0
while (meu != '*\n'):
    vet = meu.split('\n')
    mineName[mineQtd] = vet[0]
    arq = open(vet[0], 'r')
    v = arq.read()
    mineLen[mineQtd] = len(v)
    arq.close()
    mineMask[mineQtd] = qtdPkt(mineLen[mineQtd])*[1] # ((mineLen[mineQtd]-1)/pktLen+1)*[True]
    mineQtd = mineQtd+1
    meu = file.readline()
#------------------------------------
#inicializa vetores dos arquivos que eu quero
wantName = (qtdTotal - mineQtd) * ['']
wantLen = (qtdTotal - mineQtd) * [0]
wantFull = (qtdTotal - mineQtd) * [0.1]
wantMask = (qtdTotal - mineQtd) * [[0]]
#------------------------------------

# le quais arquivo quero
meu = file.readline()
wantQtd = 0
while (meu != ''):
    vet = meu.split()
    wantName[wantQtd] = vet[0]
    vet1 = vet[1].split('\n')
    wantLen[wantQtd] = int(vet1[0])
    wantMask[wantQtd] = qtdPkt(wantLen[wantQtd])*[0] #((wantLen[mineQtd]-1)/pktLen+1)*[False]
    wantFull[wantQtd] = 0.0 # porcetagem de quanto eu tenho da arquivo
    wantQtd = wantQtd + 1
    meu = file.readline()
file.close()
#------------------------------------
#------------------------------------

# loop principal
t0 = time.time()
print("1 - Status")
print("2 - Sair")
while(1):
    t1 = time.time()
    if(t1-t0 > timeout):
        s.send(str(qtdTotal)) # quantidade total de arquivos
        s.recv(1024) # evitar enviar tudo junto
        s.send(str(mineQtd)) # quantidade de arquivos que eu tenho
        s.recv(1024) # evitar enviar tudo junto
        s.send(str(wantQtd)) # quantidade de arquivos que eu quero
        s.recv(1024) # evitar enviar tudo junto
        for i in range(mineQtd):
            s.send(mineName[i]) # nome de um arquivo que o cliente tem
            s.recv(1024) # evitar enviar tudo junto
            s.send(str(mineLen[i])) # tamanho de cada arquivo que o cliente tem
            s.recv(1024) # evitar enviar tudo junto

        for i in range(wantQtd):
            s.send(wantName[i]) # nome de um arquivo que o cliente quer
            s.recv(1024) # evitar enviar tudo junto
            s.send(str(wantLen[i])) # tamanho de cada arquivo que o cliente quer
            s.recv(1024) # evitar enviar tudo junto
            s.send(str(wantFull[i])) # envia a porcentagem do arquivo
            s.recv(1024) # evitar enviar tudo junto
            if(wantFull[1] != 0.0):
                for j in range(qtdPkt(wantLen[i])):
                    s.send(str(wantMask[i][j])) # quais pacote de um arquivo o cliente quer
                    s.recv(1024) # evitar enviar tudo junto
        t0 = time.time()
#-----------------------------------------------
##################################################################################

# if(server):
#     nome = conn.recv(1024)
#     arq = open(nome,'r')
#     v = arq.read()
#     conn.send(str(len(v)))
#     conn.recv(1024)
#     for i in range((len(v)-1)/pktLen+1):
#         conn.send(v[(i*pktLen):((i+1)*pktLen)])
#         print(i)
#         conn.recv(1024)

# if(not server):

#     nome = raw_input("nome do arquivo: ")
#     conn.send(nome)

#     tam=int(conn.recv(1024))
#     v=tam*['a']
#     conn.send("haha")

#     #recebo
#     for i in range((tam-1)/pktLen+1):
#         x=conn.recv(1024)

#         v[i] = x
#         print(i)
#         conn.send("haha")
#     r=''
#     #concateno
#     for i in range((tam-1)/pktLen+1):
#        r=r+v[i] 
#     arq = open(nome,'w')
#     arq.write(r)
# arq.close()

s.close()


