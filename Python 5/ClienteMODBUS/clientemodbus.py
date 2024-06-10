from pyModbusTCP.client import ModbusClient
from time import sleep
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
#from pymodbus.constants import Endian

class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self, server_ip,porta,scan_time=1): # scan_time: tempo de varredura
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip,port = porta) # Passa o ip e a porta do servidor 
        self._scan_time = scan_time # scan_time é o intervalo de tempo entre uma leitura e outra

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        
        try:
            self._cliente.open() # Conexão com o servidor
            atendimento = True
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração | 4- Sair ): ")
                
                if sel == '1':
                    tipo = input ("""Qual tipo de dado deseja ler? (1- Holding Register |2- Coil |3- Input Register |4- Discrete Input | 5- Float | 6- Holding Registers como bits individuais.) :""") # registrador, bobina, registrador de entrada, entrada discreta, float
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    nvezes = input ("Digite o número de vezes que deseja ler: ")
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo), int(addr))}") # Método lerDado recebe o tipo e o endereço
                        sleep(self._scan_time) # sleep do tempo de varredura
                elif sel =='2':
                    tipo = input ("""Qual tipo de dado deseja escrever? (1- Holding Register |2- Coil |3- Float | 4- Holding Registers como bits individuais.) :""")
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    valor = input (f"Digite o valor que deseja escrever: ") # Tabela Modbus só aceita valor inteiro
                    self.escreveDado(int(tipo),int(addr),int(valor))

                elif sel=='3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant)

                elif sel =='4':
                    self._cliente.close() # Fecha a conexão
                    atendimento = False # Encerra o atendimento
                
                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ',e.args)

    def lerDado(self, tipo, addr):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.read_holding_registers(addr,1)[0] # 1: número de endereços que quer lê / vai retornar uma lista e escolhe o primeiro elemento da lista[0] que vai retornar para o cliente

        if tipo == 2:
            return self._cliente.read_coils(addr,1)[0]

        if tipo == 3:
            return self._cliente.read_input_registers(addr,1)[0]

        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr,1)[0]
        
        if tipo == 5:
            return self.lerFloat(addr)
        
        if tipo == 6:
            return self.lerbit(addr)
        
    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_single_register(addr,valor) # endereço e valor

        if tipo == 2:
            return self._cliente.write_single_coil(addr,valor)
        
        if tipo == 3:
            return self.escreveFloat(addr, float(valor))
        
        if tipo == 4:
            return self.escrevebit(addr, int(valor))
        
    def lerFloat(self, addr):
        result = self._cliente.read_holding_registers(addr,2) # 2 é o número de endereços que deve ler
        decoder = BinaryPayloadDecoder.fromRegisters(result)
        return decoder.decode_32bit_float()
        #decoder = BinaryPayloadDecoder.fromRegisters(result, byteorder=Endian.BIG, wordorder=Endian.LITTLE) # Big Endian (bit mais significativo primeiro) / Little Endian para palavra (palavra menos significativo primeiro)
        #decoded = decoder.decode_32bit_float() # Decodifica para um valor float de 32 bits
        #return decoded

    def escreveFloat(self, addr,valor):#tirei o float
        builder = BinaryPayloadBuilder()
        builder.add_32bit_float(float(valor))
        return  self._cliente.write_multiple_registers(addr,builder.to_registers())
        #payload = builder.to_registers()
        #return self._cliente.write_multiple_registers(addr,payload)

    def lerbit(self, addr):
        result = self._cliente.read_holding_registers(addr,1)
        decoder = BinaryPayloadDecoder.fromRegisters(result)
        lst = decoder.decode_bits()[::-1]+decoder.decode_bits()[::-1]
        return lst
    
    def escrevebit(self, addr,valor):
        bit = int(input("Qual o bit você deseja alterar ?"))
        result = self._cliente.read_holding_registers(addr,1)
        decoder = BinaryPayloadDecoder.fromRegisters(result)
        lst = decoder.decode_bits()[::-1]+decoder.decode_bits()[::-1]

        lst[bit] = int(valor)   
            
        builder = BinaryPayloadBuilder()
        builder.add_bits(lst)
        return  self._cliente.write_multiple_registers(addr,builder.to_registers())
    
        
