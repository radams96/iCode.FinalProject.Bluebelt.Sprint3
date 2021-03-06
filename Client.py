import socket                                   #Import socket features.
import time                                     #Import time fetaures.

mySocket = socket.socket()                      #Create a socket.
host = "W.X.Y.Z"                                #Set the host IP of the intended connection.
port = 12345                                    #Set port to 12345, a common port for program testing.
mySocket.connect((host,port))                   #Connect to the given IP through the given port.

while True:                                     #Loop constantly.
    response = input("Send Message?")           #Get user input.
    if(response == "yes"):                      #If yes, send a message of 'Y'.
        sentString = 'Y'
        encoded = sentString.encode()
        mySocket.send(encoded)
        time.sleep(3)
    elif(response == "no"):                     #If no, send message 'N' and terminate the loop.
        sentString = 'N'
        encoded = sentString.encode()
        mySocket.send(encoded)
        break
    else:                                       #Invalid response catch-all.
        print("Invalid response.")
        time.sleep(3)

mySocket.close()                                #Close the previously opened socket.
