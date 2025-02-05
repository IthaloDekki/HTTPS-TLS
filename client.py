import socket
import ssl

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 4433
SERVER_CERT = 'server.crt' # Certificado

# Cria um contexto SSL/TLS para o cliente
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) #TLS
context.load_verify_locations(SERVER_CERT)

context.verify_mode(ssl.CERT_REQUIRED) # Exige a verificação do certificado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock: # Envolve o socket com a camada SSL/TLS
        ssock.connect((HOST, PORT))
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data = ssock.recv(1024) # Recebe a resposta do servidor (até 1024 bytes)
        print(f"Recebido: {data.decode('utf-8')}")