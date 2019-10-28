#SeokinYoonProgrammingAssignment1
from socket import *
import sys #for exit
serverName = '10.89.197.28'
serverPort = 12000

while True:
    try:
        answer = input("CHOOSE A PROTOCOL\t[UDP]/[TCP]\t: ")
    
#UDP
        if answer == "UDP":
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            while True:
                #clientSocket = socket(AF_INET, SOCK_DGRAM)
                message = input('INPUT LOWER CASE SENTENCE : ')       
                if message == 'bye':
                    print("SHUTTING DOWN")
                    message = "TERMINATE"
                    clientSocket.sendto(message.encode(), (serverName, serverPort))
                    clientSocket.close()
                    break
                    
                else:
                    clientSocket.sendto(message.encode(), (serverName, serverPort))
                    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                    print("SERVER REPLY : ", modifiedMessage.decode())
                    print("SERVER ADDRESS : ", serverAddress)
                    
                    """
                    while True:
                        answer = input("[CONTINUE]\tOR\t[TERMINATE]\tPROGRAM\n<C>/<T>:\t")
                        if answer == 'C':
                            print("You have chosen [CONTINUE]")
                            break
                        elif answer == 'T':
                            print("You have chosen [TERMINATE]")
                            message = "TERMINATE"
                            clientSocket.sendto(message.encode(), (serverName, serverPort))
                            clientSocket.close()
                            sys.exit()
                    """                        
            
            sys.exit()
                            
            
#TCP
        elif answer== "TCP":
            clientSocket = socket(AF_INET, SOCK_STREAM) #Connection Oriented TCP Protocol
            clientSocket.connect((serverName, serverPort))
            sentence = clientSocket.recv(1024)
            print(sentence.decode())
            
            while True:
                
                sentence = input("INPUT LOWER CASE SENTENCE : ")
                if sentence == 'bye':
                    print("SHUTTING DOWN")
                    break
                clientSocket.send(sentence.encode())    
                modifiedSentence = clientSocket.recv(1024)
                print("FROM SERVER : ", modifiedSentence.decode())
                
            
            clientSocket.close()
            sys.exit()
        
    except (ValueError, TypeError, NameError, RuntimeError, OSError):
        print("OOPS! SOMETHING WENT WRONG. PLEASE CHECK THE CONNECTION AND TRY AGAIN.")
    except (ConnectionResetError):
        print("AN EXISTING CONNECTION WAS CLOSED BY THE REMOTE HOST. PLEASE WAIT AND TRY AGAIN.")
    except (ConnectionRefusedError):
        print("THE SERVER IS NOT READY YET. PLEASE WAIT AND TRY AGAIN.")
    


    
