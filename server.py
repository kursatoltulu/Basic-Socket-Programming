import socket
import mysql.connector

# Define database connection parameters
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="35453545",
    database="inovatexercise"
)
mycursor = mydb.cursor()

# Define server parameters
host = "127.0.0.1"
port = 9999
size = 1024

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(2)
print("Server is listening at {}:{}".format(host, port))

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print("Client {} connected".format(client_address))

    # Receive data from the client
    data = client_socket.recv(size)
    if data:
        # Decode the received data
        message = data.decode("utf-8")

        # Switch-case structure to handle different client requests
        if message == "1":
            mycursor.execute("SELECT NAME,SURNAME FROM personnel ORDER BY RAND() LIMIT 1")
            result = mycursor.fetchall()

            # Send a response to the client
            response = "Result: {}".format(result)
            client_socket.sendall(response.encode("utf-8"))

        elif message == "2":
            mycursor.execute("SELECT NAME,SURNAME FROM personnel ORDER BY RAND() LIMIT 1")
            result = mycursor.fetchall()
            mydb.commit()

            # Send a response to the client
            response = "Result: {}".format(result)
            client_socket.sendall(response.encode("utf-8"))

        elif message == "3":
            mycursor.execute("SELECT * FROM personnel ")
            result = mycursor.fetchall()
            mydb.commit()

            # Send a response to the client
            response = "Result: {}".format(result)
            client_socket.sendall(response.encode("utf-8"))
        
        elif message == "4":
            mycursor.execute("DELETE FROM personnel ORDER BY RAND() LIMIT 1; ")
            result = mycursor.fetchall()
            mydb.commit()

            # Send a response to the client
            response = "Delete succesfull."
            client_socket.sendall(response.encode("utf-8"))

        elif message == "5":
            mycursor.execute("DELETE FROM personnel ORDER BY RAND() LIMIT 1; ")
            result = mycursor.fetchall()
            mydb.commit()

            # Send a response to the client
            response = "Delete succesfull."
            client_socket.sendall(response.encode("utf-8"))

        elif message == "6":
            mycursor.execute("DELETE * FROM personnel; ")
            result = mycursor.fetchall()
            mydb.commit()

            # Send a response to the client
            response = "Delete succesfull."
            client_socket.sendall(response.encode("utf-8"))
        
        else:
            # Handle invalid requests
            response = "Invalid request"
            client_socket.sendall(response.encode("utf-8"))

    # Close the client connection
    client_socket.close()

# Close the server socket
server_socket.close()
