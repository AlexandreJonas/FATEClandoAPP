#Servidor TCP
import socket
from threading import Thread
from cifrarMsg import *
from decifrarMsg import *

global tcp_con

def enviar():
    global tcp_con
    msg = input()
    while True:
        msg = cifrarMsg('./chaveVitorPub.txt', msg)
        # tcp_con.send(msg.encode())
        tcp_con.send(msg)
        msg = input()

# Endereco IP do Servidor
HOST = ''

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msg = decifrarMsg('./chaveJonasPri.txt', tcp_con.recv(1024))
        # msg = tcp_con.recv(1024)
        if not msg: break
        print("Cliente:",msg)
    print ('Finalizando conexao do cliente', cliente)
    tcp_con.close()
