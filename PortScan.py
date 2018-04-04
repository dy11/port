import socket



def connect(ip, port_number, delay, output):
    # Initilize the TCP socket object
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    TCP_sock.settimeout(0.01)

    try:
        result = TCP_sock.connect_ex((ip,port_number))

        # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
        if result == 0:
            output[port_number] = 'OPEN'
        else:
            output[port_number] = 'CLOSE'

        TCP_sock.close()

    except socket.error as e:

        output[port_number] = 'CLOSE'
        pass

if __name__ == "__main__":
    output = []
    for i in range(0,65536):
        output.append('')
        connect('127.0.0.1',i,1,output)
        print(i)
    for i in range(0, 65536):
        if(output[i] == 'OPEN'):
            print(i)
            print(output[i])
