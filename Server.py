#Import Required Libraries
import socket
import urllib.request
import cv2
import numpy as np

#Create Socket with the help of tcp protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="192.168.43.2"
port=1234

#Bind IP and Port no
s.bind((ip,port))
s.listen() 
csession,addr=s.accept()

#get url from ip webcam
url="http://192.168.43.1:8080/shot.jpg?rnd=86430"

#Create a stream of Images using while loop
#After recieving decode it and make sure while sending encode it into byte array 
while True:
    data = csession.recv(10000000) 
    array= np.fromstring(data,np.uint8)
    photo = cv2.imdecode(array,cv2.IMREAD_COLOR)  
    
    if type(photo) is type(None):
        pass
    else:
        cv2.imshow("Server screen",photo)
        if cv2.waitKey(10)==13:
            break
            
    imgResp = urllib.request.urlopen(url)
    x = imgResp.read()
    csession.sendall(x)

cv2.destroyAllWindows()
