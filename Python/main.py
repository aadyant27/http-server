import socket
from Logger import Logger


def init_server():
    # Initialize the logger
    logger = Logger("http_server_python")

    # Create a server socket
    server_socket = socket.create_server(('localhost', 4221), reuse_port=True)
    # Accept a connection
    conn, addr = server_socket.accept()
    logger.info(f"Connection from {addr}")

    return server_socket, conn, addr, logger


def main():
    # Initialize the server
    server_socket, conn, addr, logger = init_server()

    '''
    It is important to read the data from the connection before sending a response(even if you don't need it)
    Otherwise, the client may not receive the response.
    It's because of the way TCP works. When you send a response, the socket buffer may not be flushed until you read from it.
    '''
    data = conn.recv(1024)
    response = "HTTP/1.1 200 OK\r\n\r\n Hello world"
    conn.sendall(response.encode())


if __name__ == "__main__":
    main()
