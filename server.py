from socket import *

# Local information
localIP = "127.0.0.1"
localPort = 1050
bufferSize = 1024

# Create Server Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind to local ip and address
serverSocket.bind((localIP, localPort))

# Notify server is on
print("The Server Is On :)")

# Loop to receive and send messages back
while (True):
    # Listen for incoming messages
    receivedMsg = serverSocket.recvfrom(bufferSize)

    # Format message and address
    clientMsg= receivedMsg[0]
    clientAddress = receivedMsg[1]
    clientMsg = clientMsg.decode()

    # Print message to screen
    print(clientMsg)

    # Send the message back to client
    returnMsg = clientMsg.encode()
    serverSocket.sendto(returnMsg, clientAddress)

# Close server
serverSocket.close()

