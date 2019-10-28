#SeokinYoonProgrammingAssignment1
from socket import *
serverPort = 12000

while True:
      try:
            answer = input("CHOOSE A PROTOCOL\t[UDP]/[TCP]\t: ")
      
#UDP
            if answer == "UDP":
                  
                  while True:
                        serverSocket = socket(AF_INET, SOCK_DGRAM)
                        serverSocket.bind(('', serverPort))
                        print("THE SERVER IS READY TO RECEIVE [UDP]")
                        
                        
                        while True:
                            message, clientAddress = serverSocket.recvfrom(2048)
                            addressData = clientAddress#[0]
                            fix = clientAddress[1]
                            

                            if message.decode() == "TERMINATE":
                                  print("DISCONNECTED FROM PREVIOUS CLIENT")
                                  break
                                  
                            print("RECEIVED : ", message.decode(),"\tCLIENT ADDRESS : ", addressData)
                            
                            oldMessage = message.decode()
                            newMessage = ['']*len(oldMessage)
                            newMessage[::2] = oldMessage[::2].upper()
                            #print(newMessage)
                            newMessage[1::2] = oldMessage[1::2].lower()
                            #print(newMessage)
                            newMessage = ''.join(newMessage)
                            serverSocket.sendto(newMessage.encode(), clientAddress)
                            print("SENT : ", newMessage)
                            
                        serverSocket.close()

                
                
#TCP
            if answer == "TCP":
                  
                  while True:
                        serverSocket = socket(AF_INET, SOCK_STREAM)
                        serverSocket.bind(('',serverPort))
                        serverSocket.listen(1)
                        print('THE SERVER IS READY TO RECEIVE [TCP]')
                        
                        while True:
                              connectionSocket, addr = serverSocket.accept()
                              print('CONNECTION FROM:\t', addr)
                              ip = addr[0]
                              greetings = "'THANK YOU FOR CONNECTING'\t#SERVER"
                              connectionSocket.send(greetings.encode())
                              
                              while True:
                                    
                                    sentence = connectionSocket.recv(1024).decode()
                                    if len(sentence) == 0:
                                          print("DISCONNECTED FROM PREVIOUS CLIENT")
                                          #connectionSocket.close()
                                          break
                                          
                                    print('The server has received a message from the client')
                                    print("RECEIVED :\t", sentence, "\tIP : ", ip)
                                    
                                    
                                          #Capitalizing Odd Entry Characters
                                    modifiedSentence = ['']*len(sentence)     
                                    modifiedSentence[::2] = sentence[::2].upper()
                                          #print(modifiedSentence)
                                    modifiedSentence[1::2] = sentence[1::2].lower()
                                          #print(modifiedSentence)
                                    modifiedSentence = ''.join(modifiedSentence)
                                    print("SENT :\t", modifiedSentence)
                                          #capitalizedSentence = sentence.upper()
                                    connectionSocket.send(modifiedSentence.encode())
                              
                              
                              connectionSocket.close()
                              break
                  
      except (ValueError, TypeError, NameError, RuntimeError, OSError):
            print("OOPS! SOMETHING WENT WRONG. PLEASE CHECK THE CONNECTION AND TRY AGAIN.")
            connectionSocket.close()
            serverSocket.close()
      except (ConnectionResetError):
            print("AN EXISTING CONNECTION WAS CLOSED BY THE REMOTE HOST. WAITING FOR ANOTHER CONNECTION.")
            connectionSocket.close()
            serverSocket.close()
      except (ConnectionRefusedError):
            print("NOT READY YET. PLEASE WAIT AND TRY AGAIN.")
            connectionSocket.close()
            serverSocket.close()
      

