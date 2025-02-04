import socket
import ssl

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 4433
SERVER_CERT = 'server.crt'

# Cria um socket TCP/IP
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(SERVER_CERT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.connect((HOST, PORT))
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data = ssock.recv(1024)
        print(f"Recebido: {data.decode('utf-8')}")