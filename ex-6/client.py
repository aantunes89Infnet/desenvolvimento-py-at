import socket
import pickle

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 8000)

client_skt.connect(address)

while True:
    msg = input("Digite nome do arquivo: ")
    client_skt.send(msg.encode('ascii'))

    if msg == 'exit':
        break

    content = client_skt.recv(1024)
    decoded_content = pickle.loads(content)
    print("---------------ARQUIVOS---------------")
    for file in decoded_content:
        print(file)
    print("--------------------------------------")


client_skt.close()
