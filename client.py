from socket import *

# Server Information
hostIP = '127.0.0.1'
clientPort = 1000
serverAddress = (hostIP,1050)
bufferSize = 1024

# Create Client Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Message for server
msg = "HELLO"

# Encode message to send
encodedMsg = msg.encode()

# Send to server
clientSocket.sendto(encodedMsg, serverAddress)

# Receive message back
serverMsg = clientSocket.recvfrom(bufferSize)

# Decode Message
serverMsg = serverMsg[0].decode()

# Print message sent from server to screen
print(serverMsg)

# End Client
clientSocket.close()
