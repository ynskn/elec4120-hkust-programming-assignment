# Programming Assignment 2 
# A simple HTTP Client
# SEOKIN YOON 20163767


from socket import *
import sys      #   FOR EXIT
urlCount = 0

while True:
    
    i = 0
    pathName = ''


    url = input ("GIVE ME A URL OF A WEBSITE :   ")     #   ENTER THE URL OF A WEBSITE YOU WANT TO VISIT
    print ('THE URL YOU HAVE GIVEN IS : %s' %(url))


    if url=="bye":
        print ("GOOD BYE")
        break

    
    domain = url.split('//')[-1].split('/')[0]      #   GETTING THE HOST NAME OF URL
    path = url.split('//')[-1].split('/')[1:]       #   GETTING THE PATH NAME


    if i == len(path):  #   IF THERE IS NO PATH
        pathName = '/'
        
    while i < len(path):
        pathName += '/' + path[i] 
        i = i+1
        
    print ('THE HOST NAME IS : %s' %(domain))
    print ('THE PATH NAME IS : %s' %(pathName))

    serverName = domain
    serverPort = 80         #   HTTP SOCKET


    clientSocket = socket(AF_INET, SOCK_STREAM)     #   CONNECTION ORIENTED TCP PROTOCOL WILL BE USED
    clientSocket.connect((serverName, serverPort))


    request = 'GET %s HTTP/1.1\r\n' %(pathName) + 'Host:%s\r\n\r\n' %(serverName)   #   GET REQUEST WILL BE SENT
    clientSocket.send(request.encode())
    print(request)
    print("-----------------------------\n")


    response = '1'  
    index = 1
    saveItHere = []

    

    while len(response) > 0:
        response = clientSocket.recv(1024)
        CRLFposition = response.decode().find("\r\n\r\n")
        statusCode = response.decode().find("200 OK")
        
        #print(response.decode())
        if CRLFposition != -1 and index:
            print(response.decode()[:CRLFposition])     #   PRINT THE RESPONSE ONLY
            print("\n--------------------\n")
            saveItHere.append(response.decode()[CRLFposition:])     #   HTML FILE ARCHIVED 
            index = 0
                        
        elif index != 1:
            saveItHere.append(response.decode())   #   HTML FILE MIA
            
        if statusCode != -1:    #   STATUS CODE IS 200

            urlCount += 1
            fileName = str(urlCount) + '.html'  #   HOW MANY URLS ARE THERE?

    save = input ("WOULD YOU LIKE TO SAVE THIS FILE?\t(Y / N):\t")
    if save == 'Y':
            
    #if urlCount >= 1:
         
        fo = open(fileName, "wb")               
        savedString = ''.join(saveItHere)
        fo.write(savedString.encode())
        fo.close()
                
                
        print ("#############################################")
        print ("SUCCESSFULLY CREATED FILE")
        print ("#############################################")
        print ("FILE NAME IS :  " + fileName)
        print ("#############################################")
        
    else:
        
        continue
        

                      
    
    clientSocket.close()
    
