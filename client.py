import socket
import sqlite3

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"
port = 9999

# connect the client to the server
client_socket.connect((host, port))

# connect to SQLite database
conn = sqlite3.connect('client.db')
cursor = conn.cursor()


while True:
    # get user input
    print('1. Send a specific personnel to a specific client.')
    print('2. Send a specific personnel to all clients.')
    print('3. Send all personnel to all clients.')
    print('4. Delete a specific personnel from a specific client.')
    print('5. Delete a specific personnel from all clients.')
    print('6. Delete all  personnel from all clients.')
    cmd = input("Enter a command (add <name> <surname> <ssn>, delete <name>, exit) or choose number: ")

    # send the command to the server
    client_socket.sendall(cmd.encode())

    # receive the server response
    data = client_socket.recv(1024)

    # print the response
    print(data.decode())

    # save data to SQLite database if adding data
    if cmd.startswith("add"):
        name, surname, ssn = cmd.split()[1:]
        cursor.execute("INSERT INTO personnel (NAME, SURNAME, SSN) VALUES (?, ?, ?)", (name, surname,ssn))
        conn.commit()

    if cmd.startswith("delete"):
        name = cmd.split()[1:]
        cursor.execute("DELETE FROM personnel WHERE name = {}".format(name))
        conn.commit()    

    # exit if command is exit
    if cmd == "exit":
        break

# close the connection
client_socket.close()
conn.close()
