import socket

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
                self._service(con, client) #con é o objeto #só pode 1 cliente, o servidor não consegue atender mais de 1 cliente ao mesmo tempo
        except Exception as e:
            print("Erro ao inicializar o servidor", e.args)

    def _service(self, con, client):
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True: #deixa o cliente realizar quantas operações ele quiser
            try:  #no cliente manda primeiro e depois recebe, no servidor recebe primeiro depois manda
                msg = con.recv(1024) #recebe o dado codificado, msg vai ser uma lista de bytes(conjunto de bits), 1024 é o tamanho máximo de bytes que quer receber de uma vez / comunicação é assíncrona
                msg_s = str(msg.decode('ascii')) #decodifica o dado que chegou, decodifica a mensagem utilizando a tabela aascii
                resp = eval(msg_s) #processamento do dado, resolver a equação por exemplo / evaluation(string) = retorna o resultado / resp vai ser um número
                con.send(bytes(str(resp), 'ascii')) #codificação da resposta / transforma o número para uma string e depois converte a string para um vetor de bytes na codificação ascii e depois envia a resposta(send)
                print(client, " -> requisição atendida")
            except OSError as e: 
                print("Erro de conexão ", client, ": ", e.args)
                return
            except Exception as e: #todas as outras que não entram na except anterior 
                print("Erro nos dados recebidos pelo cliente ",
                      client, ": ", e.args)
                con.send(bytes("Erro", 'ascii')) #manda erro para o cliente saber que deu um erro 
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