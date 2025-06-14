import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"Hello, Server!")
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")
except ConnectionRefusedError:
    print("Could not connect to server (is it running?)")
except Exception as e:
    print(f"Client error: {e}")
