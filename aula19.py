# arquivo main.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MeuApp(App): # Classe derivada da classe App
    def build(self): # Reimplementando o método build dessa classe
        layoult = BoxLayout(orientation='vertical')
        bt1 = Button(text='Botão 1', on_release = self.foo) # on_press = self.foo: toda vez que pçressiona o botão quer rodar o foo / on_release = self.foo: quando soltar o botão
        self._ti = TextInput() # Objeto de entrada de texto # ti é uma variável local do TextInput
        layoult.add_widget(bt1)
        layoult.add_widget(self._ti) # self._ti = atributo da classe MeuApp e objeto da classe textimput
        return layoult # layoult: objeto retornado pelo build(raiz)
       # return Button(text='Botão 1') # Retorna um objeto
    def foo(self,args): # tem que colocar o args pq é no mesmo protótipo do kivy
        self._ti.text = 'Hello World' # self._ti = agora é um atributo da classe MeuApp e objeto da classe textimput / texto do text input vai mudar para Hello World
app = MeuApp()
app.run()
