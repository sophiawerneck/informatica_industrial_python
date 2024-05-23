import socket
import threading # Para transformar o servidor em multithreading


class Servidor():
    """
    Classe Servidor - API Socket
    """
    def __init__(self, host, port):
        """
        Construtor da classe servidor
        """
        self._host = host
        self._port = port
    
    def start(self):
        """
        Método que inicializa a execução do servidor
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        endpoint = (self._host,self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1)
            print("Servidor iniciado em ",self._host,": ", self._port)
            while True:
                con, client = self.__tcp.accept()
                self._service(con,client)
        except Exception as e:
            print("Erro ao inicializar o servidor",e.args)
    
    def _service(self, con, client):
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try: 
                msg = con.recv(1024)
                msg_s = str(msg.decode('ascii'))
                resp = eval(msg_s)
                con.send(bytes(str(resp),'ascii'))
                print(client," -> requisição atendida")
            except OSError as e:
                print("Erro de conexão ",client,": ",e.args)
                return  
            except Exception as e:
                print("Erro nos dados recebidos pelo cliente ",client,": ",e.args)
                con.send(bytes("Erro",'ascii'))
                return


class ServidorMT(Servidor): # Herança, classe criada para transformar o servidor em multithreading, deriva da classe Servidor
    """
    Classe Servidor MultiThread - API Socket
    """
    def __init__(self, host, port): #utiliza o construtor da classe base 
        """
        Construtor da classe ServidorMT
        """
        super().__init__(host,port) # super para invocar o construtor da classe servidor
        self.__threadPool = {} #conjunto de threads(uma para cada cliente): é um dicionário que armazena as múltiplas linhas de execução
    
    def start(self): #diferente da classe base
        """
        Método que inicializa a execução do servidor
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        endpoint = (self._host,self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1) #até aqui é igual a classe base
            print("Servidor iniciado em ",self._host,": ", self._port)
            while True: 
                con, client = self.__tcp.accept() #criar outra linha de execução para executar
                self.__threadPool[client] = threading.Thread(target=self._service,args=(con,client)) #target: função e args:argumentos da funcao(conexão e cliente) / cria um objeto da classe Thread/ cada linha de execução nova executa o método service
                self.__threadPool[client].start() #executa a Thread, o start não é bloqueante, volta para o accept estando apto a pegar outro cliente
                # sem o threading usa o self.__service(con, client)
        except Exception as e:
            print("Erro ao inicializar o servidor",e.args)

# Para múltiplos clientes utiliza o multi-thread: na primeira linha de execução está executando o método start do servidor, na segunda linha 
# executa o primeiro cliente, na próxima executa o segundo cliente em paralelo
