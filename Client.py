import socket                                   #Import socket features.
import time                                     #Import time fetaures.

s = socket.socket()                             #Create a socket.
host = "W.X.Y.Z"                                #Set the host IP of the intended connection.
port = 12345                                    #Set port to 12345, a common port for program testing.
s.connect(host, port)                           #Connect to the given IP through the given port.

while true:                                     #Loop constantly.
    response = raw_input("Send Message?")       #Get user input.
    if(response == "yes"):                      #If yes, send a message of 'Y'.
        s.send('Y')
        time.sleep(3)
    elif(response == "no"):                     #If no, send message 'N' and terminate the loop.
        s.send('N')
        break
    else                                        #Invalid response catch-all.
        print("Invalid response.")
        time.sleep(3)

s.close()                                       #Close the previously opened socket.
