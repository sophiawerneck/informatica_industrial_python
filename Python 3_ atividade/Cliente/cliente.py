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
        Método que inicializa a execução do Cliente: tenta conectar o cliente ao servidor usando o endereço IP e a porta fornecidos. Se a conexão for bem-sucedida, ele chama o método privado __method para enviar a imagem.
        
        """
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint) # connect recebe como parametro o endpoint com mesmos dados do servidor
            print("Conexão realizada com sucesso!")
            self.__method(caminho_imagem)
        except:
            print("Servidor não disponível")

    
    def __method(self, caminho_imagem): # Protocolo de envio e recebimento da imagem
        """
        Método que implementa as requisições do cliente
        """
        try:
            # Leitura da imagem 
            img = cv2.imread(caminho_imagem) # caminho_imagem = 'faces/image_0001.jpg'
            # Transforma a imagem em bytes
            _, img_bytes = cv2.imencode('.jpg', img) 
            img_bytes = bytes(img_bytes)
            # Transforma o tamnho da imagem em bytes
            tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
            # Envia o tamanho da imagem em bytes para o servidor
            self.__tcp.send(tamanho_da_imagem_codificado) 
            # Envia a imagem em bytes para o servidor
            self.__tcp.send(img_bytes) 
            # Recebe o tamanho da imagem processada
            tam_img = self.__tcp.recv(1024) 
            tam = int.from_bytes(tam_img, 'big')
            # Recebe  a imagem processada
            cont = 1024    
            img_rec = self.__tcp.recv(1024)
            while(cont<=tam):
                    img_rec += self.__tcp.recv(1024)
                    cont += 1024
            # Decodifica a imagem processada
            img2 = cv2.imdecode(np.frombuffer(img_rec, np.uint8), cv2.IMREAD_COLOR)
            # Exibe a imagem processada
            cv2.imshow('Imagem Processada', img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.__tcp.close() #fechar a conexão

        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)

