import kivy
from kivy.app import App # Classe base a geração de aplicativos utilizando o kivy
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout # BoxLayoult permite organizar os widgets de maneira sequencial
from kivy.uix.label import Label

class BasicApp(App):
    """
    Aplicativo básico Kivy
    """
    def build(self):
        """
        Constrói o aplicativo a partir de um conjunto de widgets
        :return Widget principal da aplicação
        """ # Dentro do layoult tem 3 widgets: label, botao e layoult 2
        layout = BoxLayout(orientation = 'horizontal') # widget base: layoult
        self.lb = Label(text="0") # label = widget filho 1
        bt = Button(text = "Botão 1", on_release = self.incrementar) # label = widget filho 2
        layout.add_widget(self.lb) # Insere o label
        layout.add_widget(bt) # Insere o botão
        
        
        layout2 = BoxLayout(orientation = 'vertical') # layoult 2 tem 2 widgets
        self.lb2 = Label(text="0", color=[1,0,0,1])
        self.lb3 = Label(text="0")
        layout2.add_widget(self.lb2)
        layout2.add_widget(self.lb3)
        layout.add_widget(layout2) # Adicionar o layoult 2 como filho do layoult

        return layout
    
    def incrementar(self,*args):
        self.lb.text = str(int(self.lb.text)+1) 
        self.lb2.text = str(int(self.lb2.text)+2) 
        self.lb3.text = str(int(self.lb3.text)+3) 

if __name__=='__main__':
    BasicApp().run()

