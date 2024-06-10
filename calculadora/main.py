import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class MyWidget(BoxLayout):
    expression = ""  # String para armazenar a expressão

    def armazena(self, num):
        """
        Método para funções da calculadora
        """
        if num == 'C':
            self.expression = ""
            self.ids.lb.text = '0'
        elif num == 'DEL':
            self.expression = self.expression[:-1]
            self.ids.lb.text = self.expression if self.expression else '0'
        elif num == '=':
            try:
                self.expression = str(eval(self.expression))
                self.ids.lb.text = self.expression
            except Exception as e:
                self.ids.lb.text = 'Erro'
                self.expression = ""
        else:
            if self.ids.lb.text == '0':
                self.expression = num
            else:
                self.expression += num
            self.ids.lb.text = self.expression

class CalculadoraApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()  # Retorna um objeto da classe MyWidget

if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    Window.size = (500, 600)
    Window.fullscreen = False
    CalculadoraApp().run()
'''
# Usar o eval para fazer as contas
class MyWidget(BoxLayout):
    def armazena(self,dt):
        """
        Método para funções da calculadora
        """           
        self.vet = []
        if(self.ids.zero.text == '0'):
            self.ids.lb.text = '0' # Para printar na tela esse valor
            self.vet.append('0') 
        elif(self.ids.um.text == '1'):
            self.ids.lb.text = '1' 
            self.vet.append('1') 
        elif(self.ids.dois.text == '2'):
            self.ids.lb.text = '2' 
            self.vet.append('2') 
        elif(self.ids.tres.text == '3'):
            self.ids.lb.text = '3' 
            self.vet.append('3') 
        elif(self.ids.quatro.text == '4'):
            self.ids.lb.text = '4' 
            self.vet.append('4')  
        elif(self.ids.cinco.text == '5'):
            self.ids.lb.text = '5' 
            self.vet.append('5')  
        elif(self.ids.seis.text == '6'):
            self.ids.lb.text = '6' 
            self.vet.append('6') 
        elif(self.ids.sete.text == '7'):
            self.ids.lb.text = '7' 
            self.vet.append('7') 
        elif(self.ids.oito.text == '8'):
            self.ids.lb.text = '8' 
            self.vet.append('8') 
        elif(self.ids.nove.text == '9'):
            self.ids.lb.text = '9' 
            self.vet.append('9')   
        elif(self.ids.soma.text == '+'):
            self.vet.append('+') 
            self.ids.lb.text = '+' 
        elif(self.ids.sub.text == '-'):
            self.vet.append('-') 
            self.ids.lb.text = '-' 
        elif(self.ids.mult.text == '*'):
            self.vet.append('*') 
            self.ids.lb.text = '*'   
        elif(self.ids.div.text == '/'):
            self.vet.append('/') 
            self.ids.lb.text = '/' 
        else:
            self.vet.append('=') 
            self.ids.lb.text = '=' 


class CalculadoraApp(App): # padrão do kivy vai ter que ser basic.kv
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget() # Retorna um objeto da classe MyWidget
    
if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    Window.size=(500,600)
    Window.fullscreen = False
    CalculadoraApp().run()

 Para calculadora: layoult box layolt com 3, a tela(0 q é label), outro para os outros numeros e o último para a linha de baixo
 grid layout, só utiliza label e botão

Atividade: primeiro um label em cima pra mostrar o resultados
Depois um grid layout para os quadrados iguais do meio 
Depois um box layout para os dois com tamanho diferente embaixo 
Organizar layouts, label e botões no .kv
self.ids['lb'].text = str(int(self.ids.lb.text) + 1)  # self.ids.lb.text tem acesso aos ids dos componentes do arquivo .kv
'''
