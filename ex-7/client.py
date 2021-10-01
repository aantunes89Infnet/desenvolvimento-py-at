import socket, pickle, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 8000
address = (HOST, PORT)

try:
    while True:
        msg = input("Digite qualquer mensagem para buscar memória disponível: ")
        client_socket.sendto(msg.encode('ascii'), address)
        
        
        a = time.time()
        
        try:
            response = client_socket.recvfrom(1024)
            decoded_response = pickle.loads(response[0])
        except Exception as err:
            pass
        
        b = time.time()
        
        print(b - a)

        if b - a > 5.0:
            for i in range(5):
                if decoded_response is None:
                    response = client_socket.recvfrom(1024)
                else:
                    break


        print("-------------DISK--------------")
        print(f"TOTAL MEMORY {decoded_response['total'] >> 20} MB")
        print(f"AVAILABLE MEMORY TO USE {decoded_response['available'] >>20} MB")
        print("-------------------------------")
        break
except Exception as err:
    print(err)

client_socket.close()