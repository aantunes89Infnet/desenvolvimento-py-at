import os, socket, pickle


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 8000)

server_socket.bind(address)
server_socket.listen()

(client_skt, add) = server_socket.accept()

while True:
    msg = client_skt.recv(1024)
    msg_decoded = msg.decode('ascii')

    if msg_decoded == 'exit':
        break

    file_list = []
    for f in os.listdir(msg_decoded):
        if os.path.isfile(f"{msg_decoded}/{f}"):
            file_list.append(f)

    print(file_list)
    byte_list = pickle.dumps(file_list)

    client_skt.send(byte_list)

server_socket.close()