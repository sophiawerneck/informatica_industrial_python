from pyModbusTCP.server import DataBank, ModbusServer
import random
from time import sleep


class ServidorMODBUS():
    """
    Classe Servidor Modbus
    """
    
    def __init__(self, host_ip, port): # Parâmetros: ip e porta do servidor
        """
        Construtor
        """
        self._db = DataBank() # Possui as tabelas do servidor Modbus
        self._server = ModbusServer(host=host_ip,port=port,no_block=True,data_bank=self._db) # Cria um objeto da classe ModbusServer, no_block = True cria uma thread para atender os clientes
        # A classe ModbusServer vai acessar a classe DataBank e vai permitir que os dados sejam acessíveis para o programa 
        
    def run(self):
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start() # Iniciar a execução
            print("Servidor MODBUS em execução")
            while True:
                self._db.set_holding_registers(1000,[random.randrange(int(0.95*400),int(1.05*400))]) # random para ser um valor aletório entre int(0.95*400) e int(1.05*400)(de 400 a +- 5%), 1000 é o endereço da tabela que vai armazenar o valor aleatório
                print('======================')
                print("Tabela MODBUS")
                print(f'Holding Register \r\n R1000: {self._db.get_holding_registers(1000)} \r\n R2000: {self._db.get_holding_registers(2000)}') # ler o valor na posição 1000 e 2000 e exibir
                print(f'Coil \r\n R1000: {self._db.get_coils(1000)}') # coil: bobina
                sleep(1) # A cada 1s executa
        except Exception as e:
            print("Erro: ",e.args)

# set_holding_registers(address, word_list, srv_info=None) -> Write data to server holding registers space
# get_holding_registers(address, number=1, srv_info=None) -> Read data on server holding registers space
# get_coils(address, number=1, srv_info=None) -> Read data on server coils space
    

