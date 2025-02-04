import socket
import ssl

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 4433
CERTIFICATE = 'server.crt'
PRIVATE_KEY = 'server.key'

# Cria um socket TCP/IP
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTIFICATE, keyfile=PRIVATE_KEY)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Servidor escutando em {HOST}:{PORT}...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        with conn:
            print(f"Conexão estabelecida com {addr}")
            data = conn.recv(1024)
            print(f"Recebido: {data.decode('utf-8')}")
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, Client!")