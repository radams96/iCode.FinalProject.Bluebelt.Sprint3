import socket                               #Import socket features.
import time                                 #Import time features.
import RPi.GPIo as GPIO                     #Import GPIO features, and name GPIO.

GPIO.setmode(GPIO.BOARD)                    #Set GPIO numbering convention to BOARD.
GPIO.setup(11, GPIO.OUT)                    #Set pin 11 as GPIO output.
GPIO.output(11, False)                      #Set pin 11 output to false (LED off).

def led_blink():                        #DEFINING THE LED BLINK FUNCTION.
    GPIO.output(11,True)                    #Turn on LED.
    time.sleep(1)                           #Wait for one second.
    GPIO.output(11,False)                   #Turn off LED.
    time.sleep(1)                           #Wait for one second.

s = socket.socket()                         #Create a socket.
host = "W.X.Y.Z"                            #Set the host IP of the intended connection.
port = 12345                                #Set port to 12345, a common port for program testing.
s.bind(host,port)                           #Bind to the given IP through the given port.
print "Listening..."                        #Display to user that the device is listening.
s.listen(5)                                 #Perform listen function.
c, addr = s.accept()                        #Accept message transmition.

while True:
    message = c.recv(1024)                  #Receive message and store it.
    if(message == 'Y'):                     #If message is 'Y', run led_blink()
        led_blink()
    elif(message == 'N'):                   #If message is 'N', break the loop.
        print "Closing connection..."
        break
    else:                                   #Otherwise, print invalid message received.
        print "No message received."
c.close()                                   #Close the socket.
GPIO.cleanup()                              #Cleanup the GPIO.
