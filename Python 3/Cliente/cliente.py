import socket

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

    
    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint) #connect recebe como parametro o endpoint com mesmos dados do servidor
            print("Conexão realizada com sucesso!")
            self.__method()
        except:
            print("Servidor não disponível")

    
    def __method(self): #protocolo da calculadora
        """
        Método que implementa as requisições do cliente
        """
        try:
            msg = ''
            while True:
                msg = input("Digite a operação (x para sair): ") 
                if msg == '':
                    continue
                elif msg == 'x':
                    break
                self.__tcp.send(bytes(msg,'ascii')) #cliente: manda e depois recebe, no servidor recebe e depois manda
                resp = self.__tcp.recv(1024)
                print("= ",resp.decode('ascii')) #printa a resposta no terminal
            self.__tcp.close() #fechar a conexão
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)
