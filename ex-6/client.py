import socket

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 8000)

client_skt.connect(address)

while True:
    msg = input("Digite nome do arquivo: ")
    client_skt.send(msg.encode('ascii'))

    if msg == 'exit':
        break

    content = client_skt.recv(1024)
    print(content.decode('ascii'))


client_skt.close()
