import socket, pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 8000
address = (HOST, PORT)


def receive_and_print():
    response = client_socket.recvfrom(1024)
    return pickle.loads(response[0])

try:
    while True:
        msg = input("Digite qualquer mensagem para buscar memória disponível: ")
        client_socket.sendto(msg.encode('ascii'), address)
        
        failed = False
        try:
            client_socket.settimeout(5.0)     
            confirmation = client_socket.recvfrom(1024)   
        except socket.timeout:
            for i in range(5):
                try:
                    print("tentando!!!")
                    client_socket.settimeout(5.0)     
                    confirmation = client_socket.recvfrom(1024)
                except socket.timeout:
                    failed = True
                    pass

        if failed == True:
            break
        
        response = client_socket.recvfrom(1024)
        decoded_response = pickle.loads(response[0])
                        


        print("-------------DISK--------------")
        print(f"TOTAL MEMORY {decoded_response['total'] >> 20}")
        print(f"AVAILABLE MEMORY TO USE {decoded_response['available'] >>20}")
        print("-------------------------------")
        break
except Exception as err:
    print(err)

client_socket.close()