import socket
import cv2
import os
import numpy as np

class Servidor(): 
    """
    Classe Servidor - API Socket
    """
    def __init__(self, host, port): #construtor / host é o endereço ip do servidor
        """
        Construtor da classe servidor
        """
        self._host = host #atributo protegido
        self._port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp é o objeto que instanciou na classe socket
        #primeiro parametro é a família de endereços para qual quer oferecer o serviço, segundo parametro indica se o serviço é TCP ou UDP, no caso
        #é TCP, se for UDP é SOCK_DGRAM
    def start(self): #da início ao processo do servidor
        """
        Método que inicializa a execução do servidor
        """
        endpoint = (self._host, self._port) #endpoint é uma variável local do método start, é uma tupla(imutável) / enderço ip e a porta
        try:
            self.__tcp.bind(endpoint) #passa para o bind o conjunto ip e porta / bind pode dar errado pq n sabe se existe outro programa usando a mesma porta, se tiver o sistema operaconal n vai deixar que o serviço seja realizado
            self.__tcp.listen(1) #ao executar o listen, está apto a receber as conexões dos clientes 
            print("Servidor iniciado em ", self._host, ": ", self._port) 
            while True: 
                con, client = self.__tcp.accept() #só é executado depois do cliente se conectar, é um comando bloqueante, o fluxo de execução /código para aqui: 9000
                                                  #para naquele ponto e só segue depois que um comando x é executado, con é um objeto que permite realizar a escrita e a leitura
                self._service(con, client) #con é o objeto
        except Exception as e:
            print("Erro ao inicializar o servidor", e.args)

    def _service(self, con, client):
        """
        Método que implementa o serviço de processamento de imagens
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True: #deixa o cliente realizar quantas operações ele quiser
            try:  #no cliente manda primeiro e depois recebe, no servidor recebe primeiro depois manda
                tam_img = con.recv(1024)
                tam = int.from_bytes(tam_img, 'big')
                cont = 1024
                img_rec = con.recv(1024)

                while(cont<=tam):
                    img_rec += con.recv(1024)
                    cont += 1024
                img = cv2.imdecode(np.frombuffer(img_rec, np.uint8), cv2.IMREAD_COLOR)
                # processamento
                xml_classificador = os.path.join(os.path.relpath(
                   cv2.__file__).replace('__init__.py', ''), 'data\haarcascade_frontalface_default.xml')
                face_cascade = cv2.CascadeClassifier(
                   xml_classificador)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
                # Desenha retângulos nas áreas onde as faces foram detectadas
                for (x, y, w, h) in faces:
                   cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
                con.send(tamanho_da_imagem_codificado)
                con.send(img_bytes)
                print(client, " -> requisição atendida")

            except OSError as e:
                print("Erro de conexão ", client, ": ", e.args)
                return
            except Exception as e:
                print("Erro nos dados recebidos pelo cliente ",
                      client, ": ", e.args)
                con.send(bytes("Erro", 'ascii'))
                return

'''
serviço:
 - recebe dado codificado
 - decodificar
 - processamento da requisição
 - codificação da resposta
 - envio da resposta
protocolo é a regra de comunicação entre cliente e servidor(ex.: http)
a porta de saída do cliente o programa é aleatória
'''