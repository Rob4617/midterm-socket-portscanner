import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client disconnected.")
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(b"Message received")
except Exception as e:
    print(f"Server error: {e}")
