#Import the required libraries
import socket
import cv2
import numpy as np

#create socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to server ip's and port no
s.connect(("192.168.43.2",1234))

#Connect your laptop's webcam
cap=cv2.VideoCapture(0)

#Encode the photo and send it
#Decode the recieved stream of images and display it.
while True:

    ret, frame = cap.read()
    photobytes = cv2.imencode('.jpg',frame)[1].tobytes()
    s.sendall(photobytes)

    data = s.recv(10000000)  
    array= np.fromstring(data,np.uint8)
    img = cv2.imdecode(array,-1)
   
    if type(img) is type(None):
        pass
    else:
        cv2.imshow("Clientscreen",img)
        if cv2.waitKey(10)==13:
            break

cv2.destroyAllWindows()
