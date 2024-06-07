import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '172.20.10.14'  # h ip mou
    port = 53441  # to port pou dialexa

    server_socket.bind((host, port))
    server_socket.listen(3)  # mexri 3 connections

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}") 
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message received: {data.decode()}")  # print to mynhma
            client_socket.send(data)  # steile mynhma pisto sto client

        client_socket.close()  # kleise socket

