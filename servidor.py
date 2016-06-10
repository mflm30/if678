import socket
import thread
import time

port = 8082
maxCon = 1
pktLen = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#-----------------------------------
# funcao que dado um tamnho de arquivo(bytes), retorna aquantida de pacotes
def qtdPkt(tam):
    return ((tam-1)/pktLen+1)
#-------------------------------------

conn = 10*['']

try:
    s.bind ( ('',port) )

except socket.error as e:
    print(e)
    exit(1)

s.listen(maxCon) # espera coneccao
conn[0], addr = s.accept()

while(1):
        qtdTotal = int(conn[0].recv(1024))
        conn[0].send("oi alice")
        print(qtdTotal)

        #inicializa vetores dos arquivos que eu quero
        mineName = qtdTotal * ['']
        mineLen = qtdTotal * [0]
        mineMask = qtdTotal * [[1]]
        #------------------------------------

        mineQtd = int(conn[0].recv(1024))
        conn[0].send("oi bob")
        print(mineQtd)

        #inicializa vetores dos arquivos que eu quero
        wantName = (qtdTotal - mineQtd) * ['']
        wantLen = (qtdTotal - mineQtd) * [0]
        wantFull = (qtdTotal - mineQtd) * [0.1]
        wantMask = (qtdTotal - mineQtd) * [[0]]
        #------------------------------------

        wantQtd = int(conn[0].recv(1024))
        conn[0].send("oi alice")
        print(wantQtd)

        for i in range(mineQtd):
                mineName[i] = conn[0].recv(1024)
                conn[0].send("oi bob")
                print(mineName[i])
                mineLen[i] = int(conn[0].recv(1024))
                conn[0].send("oi alice")
                print(mineLen[i])
                mineMask[i] = qtdPkt(mineLen[i]) * [1]
	
	for i in range(wantQtd):
                wantName[i] = conn[0].recv(1024)
                conn[0].send("oi bob")
                print(wantName[i])
                wantLen[i] = int(conn[0].recv(1024))
                conn[0].send("oi alice")
                print(wantLen[i])
                wantFull[i] = float(conn[0].recv(1024))
                conn[0].send("oi bob")
                if(wantFull[i] == 0.0):
                        wantMask[i] = qtdPkt(wantLen[i]) * [0]
                        print("afafad")
                else:
                        wantMask[i] = qtdPkt(wantLen[i]) * [0]
                        for j in range(qtdPkt(wantLen[i])):
                                wantMask[i][j] = int(conn[0].recv(1024))
                                conn[0].send("oi alice")
                        print("fafafad")
conn[0].close()


