from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window # Para definir o tamanho da janela
from kivy.clock import Clock # agendar uma função 
from time import sleep

class MyWidget(BoxLayout):
    _vel = [1,1] # Velocidade x e y da bola

    def move(self,dt): # Método para atualizar a posição da bola no sistema
        # sleep(0.3) deixa com leg
        self.ids.bola.x += self._vel[0] # Coordenada x do canto inferior esqurdo, soma vel nesse valor, soma 1 no x e 1 no y, a bola vai subir na diagonal
        self.ids.bola.y += self._vel[1] # Velocidade de 60 pixels por segundo no x e no y
        if self.ids.bola.x < 0 or self.ids.bola.right > self.ids.valid_region.width: # Para a bola só ficar dentro da região válida na horizontal / self.ids.bola.right > self.ids.valid_region.width: se a extremidade direita for maior que a largura da região válida
            self._vel[0] *= -1 # Inverte a velocidade
        if self.ids.bola.y < 0 or self.ids.bola.top > self.ids.valid_region.height: # Para a bola só ficar dentro da região válida na vertical
            self._vel[1] *= -1
 
      
    def command(self):
        if self.ids.bt_mover.text == "Mover": # bt_mover é o id do botão
            self._ev = Clock.schedule_interval(self.move, 1.0/60.0) # Executar uma rotina ciclicamente, no caso executar o move -> 1.0/60.0 é 60 vezes por segundo / Invoca o método move 60 vezes por segundo
            self.ids.bt_mover.text = "Parar"
        elif self.ids.bt_mover.text == "Parar":
            self._ev.cancel() # Para cancelar o evento
            self.ids.bt_mover.text = "Mover"

class MovingBallApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800,600)
    Window.fullscreen = False
    MovingBallApp().run()