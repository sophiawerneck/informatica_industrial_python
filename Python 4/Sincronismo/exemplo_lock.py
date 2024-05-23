import threading
import time


class ContaBancaria: #fazer mais de uma transferencia ao mesmo tempo
    """
    Quando o lock é utilizado, há a sincronização entre as threads do método disparar_ordens
    Quando ele não é utilizado, há uma condição de corrida que deixa o comportamento do sistema inconsistente
    """

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def transferir(self, valor):
        with self.lock: #comentar essa linha para ver oq ocorre, utliza o self.lock para cada thread ser executada uma após a outra
            #self.lock.acquire()
            saldo_atual = self.saldo #saldo_atual é variável local,, self.saldo é um atributo compartilhado entre as threads
            time.sleep(0.1) #simular um tempo da transacao(100 ms)
            saldo_atual -= valor 
            time.sleep(0.1) 
            self.saldo = saldo_atual 
            print(f'Transferência realizada: {valor} | Saldo atual: {self.saldo}')
            #self.lock.release()
        
    def disparar_ordens(self, ordens):
        thread_pool = []
        for ordem in ordens:
            thread_pool.append(threading.Thread(
                target=conta.transferir, args=(ordem,)))
            thread_pool[-1].start()
        for th in thread_pool:
            th.join() #pausar a execução do fluxo atuação até a thread em questao não parar #pausa a thread atual em detrimento de outra thread


saldo_inicial = 200 #só é exibido depois que realizou todas as operações

conta = ContaBancaria(saldo_inicial)

ordens_para_transferencia = [50, 70, 20, 60] #ao final o saldo é 0

conta.disparar_ordens(ordens_para_transferencia)

print(f'Saldo final: {conta.saldo}')

#vai ter 5 threads, uma para cada tranferência(4 transferências) e 1 para a main