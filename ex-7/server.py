import socket, pickle
import time

import psutil

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 8000
address = (HOST, PORT)

server_socket.bind(address)

while True:
    (msg, client) = server_socket.recvfrom(1024)
    try:
        content = msg.decode('ascii')
        memory = psutil.virtual_memory()
        print(content)

        total = memory.total
        available = memory.available
        memory_bytes = pickle.dumps({'total': total, 'available': available})
        time.sleep(7)
        server_socket.sendto(memory_bytes, client)

    except Exception as err:
        print((err))

server_socket.close()
