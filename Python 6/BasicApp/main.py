import kivy
from kivy.app import App # importação da classe base para a geração de aplicativos
from kivy.uix.boxlayout import BoxLayout # BoxLayoult permite a organização dos widgets de maneira sequencial
from kivy.config import Config

class MyWidget(BoxLayout): # Classe MyWidget é derivada do BoxLayout
    def changelb(self):
        """
        Método simples para incremento do valor mostrado no label
        """
        self.ids['lb'].text = str(int(self.ids.lb.text) + 1)  # self.ids.lb.text tem acesso aos ids dos componentes do arquivo .kv / self.ids(dicionário com todos os id) -> escohe o id que quer usar
        #str(int(self.ids.lb.text) + 1): incrementa 1 no valor que está no texto e transforma para string
class BasicApp(App): # padrão do kivy vai ter que ser basic.kv # BasicApp é o aplicativo base 
    def build(self): # método build serve para construir o aplicativo
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget() # Retorna um objeto da classe MyWidget, retorna o widget que queremos mostrar na tela
 
if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicApp().run() # Rodar o BasicApp

# Para calculadora: layoult box layolt com 3, a tela(0 q é label), outro para os outros numeros e o último para a linha de baixo
# grid layout, só utiliza label e botão