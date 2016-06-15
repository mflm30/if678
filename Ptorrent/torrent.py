"""
@disciplina: IF678 - Infra-Estrutura de Comunicação (IF678EC)  2016.1
@nome: Ptorrent
@authores: Matheus Moreira (mflm30)
"""
from hashlib import md5, sha1
from random import choice
import socket
from struct import pack, unpack
from threading import Thread
from time import sleep, time
import types
from urllib import urlencode, urlopen
from util import collapse, slice

#Retorna a informação de dicionário para um arquivo torrent.
def info_discionario(file):
	with open(file) as f:
		contents = f.read()
	# varia de acordo com o tamanho do arquivo
	tamanho_pedaco = 524288 
	# objeto info 
	info = {}
	# adicionando informações
	info["tamanho_pedaco"] = tamanho_pedaco
	info["tamanho"] = len(contents)
	info["nome"] = file
	info["md5sum"] = md5(contents).hexdigest()
	# Generate the pieces
	pieces = slice(contents, tamanho_pedaco)
	pieces = [ sha1(p).digest() for p in pieces ]
	info["pieces"] = collapse(pieces)

	return info

# Retorna o conteúdo codificado de um arquivo torrent.
def torrent_arquivo(file = None, tracker = None, comment = None):
	if not file:
		raise TypeError("torrent_arquivo requer pelo menos um arquivo.")
	if not tracker:
		raise TypeError("torrent_arquivo requer pelo menos um tracker.")
    # objeto torrent pae
	torrent = {}
	# Nós só temos um tracker, então essa é pae
	if type(tracker) != list:
		torrent["announce"] = tracker
	# Multiple trackers, first is announce, and all go in announce-list
	elif type(tracker) == list:
		torrent["announce"] = tracker[0]
		# And for some reason, each needs its own list
		torrent["announce-list"] = [[t] for t in tracker]

	torrent["creation date"] = int(time())
	torrent["created by"] = CLIENT_NAME
	if comment:
		torrent["comment"] = comment

	torrent["info"] = info_discionario(file)

	return encode(torrent)
