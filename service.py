import socket
import ssl

HOST = '127.0.0.1' # Endereço IP do servidor (localhost)
PORT = 4433
CERTIFICATE = 'server.crt' # certificado
PRIVATE_KEY = 'server.key'  # Chave Privada

# Cria um socket TCP/IP
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) #TLS
context.load_cert_chain(certfile=CERTIFICATE, keyfile=PRIVATE_KEY)  # Carrega o certificado e a chave privada

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT)) 
    sock.listen(5)
    print(f"Servidor escutando em {HOST}:{PORT}...")

    with context.wrap_socket(sock, server_side=True) as ssock: 
        conn, addr = ssock.accept() # Conexão com cliente
        with conn:
            print(f"Conexão estabelecida com {addr}")
            data = conn.recv(1024)  # Recebe dados do cliente (até 1024 bytes)
            print(f"Recebido: {data.decode('utf-8')}")
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, Client!")