import socket

def client():
    # create a client socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to a server
    clientsocket.connect(('', 5500))
    print("Connection made to port 5500")

    # Recieve data
    data = clientsocket.recv(1024)

    # Close client socket
    clientsocket.close()

    # return message from server
    return data.decode()

if __name__ == '__main__':
    print(client())



# 192.168.1.9
# 66.91.106.98