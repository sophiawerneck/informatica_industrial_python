import socket
import cv2
import os
import numpy as np

# Código que o cliente envia uma imagem para o Servidor, e recebe a imagem com um retângulo azul ao redor da face
# A imagem é exibida quando o cliente a recebe

class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):#define o ip e a porta do servidor, mesmos dados do servidor, tem que colocar porta 9000 igual do cliente
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip 
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP pq cliente tmb é TCP

    
    def start(self, caminho_imagem):
        """
        Método que inicializa a execução do Cliente
        """
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint) # connect recebe como parametro o endpoint com mesmos dados do servidor
            print("Conexão realizada com sucesso!")
            self.__method(caminho_imagem)
        except:
            print("Servidor não disponível")

    
    def __method(self, caminho_imagem): # Protocolo de envio de imagem
        """
        Método que implementa as requisições do cliente
        """
        try:
            img = cv2.imread(caminho_imagem) # caminho_imagem = 'faces/image_0001.jpg', lê a imagem
            _, img_bytes = cv2.imencode('.jpg', img) # Transforma a imagem em bytes
            img_bytes = bytes(img_bytes)
            tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
            # Envia o tamanho da imagem
            self.__tcp.send(tamanho_da_imagem_codificado) # manda o tamanho da imagem para o servidor
            self.__tcp.send(img_bytes) # manda a imagem em bytes para o servidor
            tam_img = self.__tcp.recv(1024) 
            tam = int.from_bytes(tam_img, 'big')
            cont = 1024    
            img_rec = self.__tcp.recv(1024)
            while(cont<=tam):
                    img_rec += self.__tcp.recv(1024)
                    cont += 1024
            img2 = cv2.imdecode(np.frombuffer(img_rec, np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('Imagem Processada', img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.__tcp.close() #fechar a conexão

        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)
