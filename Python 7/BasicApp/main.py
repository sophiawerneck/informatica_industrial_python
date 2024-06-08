import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window # Alterar tamanho da tela

class MyWidget(FloatLayout):
    pass

class BasicApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()
 
if __name__ == '__main__':
    Window.size=(800,600) # =(1024,68) é a tela cheia
    Window.fullscreen = False
    BasicApp().run()