import socket
from Logger import Logger


def main():
    logger = Logger("http_server_python")
    # Create a server socket
    server_socket = socket.create_server(('localhost', 4221), reuse_port=True)
    # Accept a connection
    conn, addr = server_socket.accept()
    logger.info(f"Connection from {addr}")


if __name__ == "__main__":
    main()
