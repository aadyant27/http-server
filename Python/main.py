import socket
from Logger import Logger

logger = Logger("http_server_python")


def init_server():
    # Initialize the logger
    # Create a server socket
    server_socket = socket.create_server(('localhost', 4221), reuse_port=True)
    logger.info("Server started on port 4221")
    # Accept a connection
    conn, addr = server_socket.accept()
    logger.info(f"Connection from {addr}")

    return server_socket, conn, addr


def extract_request_props(request_data):
    lines = request_data.split('\r\n')
    method, url, http_version = lines[0].split(' ')

    return method, url, http_version


def extract_header(request_data):
    # Extract headers from the request data
    headers = {}
    lines = request_data.split('\r\n')[1:]
    for line in lines:
        if line:
            key, value = line.split(': ', 1)
            headers[key] = value
    return headers


def helper_generate_GET_response(url, data):
    if url == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif url.startswith('/echo/'):
        body = url[len('/echo/'):]
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: {0}\r\n"
            "\r\n"
            "{1}"
        ).format(len(body), body)
    elif url.startswith('/user-agent'):
        headers = extract_header(data)

        body = headers['User-Agent']
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: {0}\r\n"
            "\r\n"
        ).format(len(body))
        response += body
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    logger.info(f"GET-request RESPONSE:\n\n{response}")
    return response


def main():
    # Initialize the server
    server_socket, conn, addr = init_server()

    '''
    It is important to read the data from the connection before sending a response(even if you don't need it)
    Otherwise, the client may not receive the response.
    It's because of the way TCP works. When you send a response, the socket buffer may not be flushed until you read from it.
    '''
    data = conn.recv(1024)
    logger.info(f"HTTP Request:\n\n{data.decode()}")

    method, url, http_version = extract_request_props(data.decode())
    if method == "GET":
        response = helper_generate_GET_response(url, data.decode())

    conn.sendall(response.encode())


if __name__ == "__main__":
    main()
