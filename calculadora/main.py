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
            if self.expression:
                self.ids.lb.text = self.expression  # Define o texto do Label como a expressão atual
            else:
                self.ids.lb.text = '0'  # Define o texto do Label como '0' se não houver uma expressão válida
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
 Para calculadora: layoult box layolt com 3, a tela(0 q é label), outro para os outros numeros e o último para a linha de baixo
 grid layout, só utiliza label e botão

Atividade: primeiro um label em cima pra mostrar o resultados
Depois um grid layout para os quadrados iguais do meio 
Depois um box layout para os dois com tamanho diferente embaixo 
Organizar layouts, label e botões no .kv
self.ids['lb'].text = str(int(self.ids.lb.text) + 1)  # self.ids.lb.text tem acesso aos ids dos componentes do arquivo .kv
'''

