import kivy
kivy.require("1.10.1")
from kivy.uix.button import Button, Label
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger
from kivy.app import App

class Box(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(Box, self).__init__(*args, **kwargs)
        self.label1= Label(text="0")
        self.add_widget(self.label1)
        boxik = BoxLayout(orientation="vertical")
        self.add_widget(boxik)
        self.vysledek_label = Label(text="0")
        self.add_widget(self.vysledek_label)
        
        boxik.tlacitko1 = Button(text="1", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko1)
        
        boxik.tlacitko2 = Button(text="2", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko2)
        
        boxik.tlacitko3 = Button(text="3", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko3)
        
        boxik.tlacitko4 = Button(text="4", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko4)
        
        boxik.tlacitko5 = Button(text="5", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko5)
        
        boxik.tlacitko6 = Button(text="6", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko6)
        
        boxik.tlacitko7 = Button(text="7", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko7)
        
        boxik.tlacitko8 = Button(text="8", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko8)
        
        boxik.tlacitko9 = Button(text="9", on_press=self.NapisCislo1)
        boxik.add_widget(boxik.tlacitko9)
        
        boxik.tlacitko1 = Button(text="1", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko1)
        
        boxik.tlacitko2 = Button(text="2", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko2)
        
        boxik.tlacitko3 = Button(text="3", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko3)
        
        boxik.tlacitko4 = Button(text="4", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko4)
        
        boxik.tlacitko5 = Button(text="5", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko5)
        
        boxik.tlacitko6 = Button(text="6", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko6)
        
        boxik.tlacitko7 = Button(text="7", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko7)
        
        boxik.tlacitko8 = Button(text="8", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko8)
        
        boxik.tlacitko9 = Button(text="9", on_press=self.NapisCislo2)
        boxik.add_widget(boxik.tlacitko9)
        
        boxik.tlacitko11 = Button(text="Exit", on_press=self.Exit)
        boxik.add_widget(boxik.tlacitko11)

    def NapisCislo1(self, *args):
        self.vysledek_label.text = Button
        
    def NapisCislo2(self, *args):
        self.label1.text = Button

    if self.vysledek_label.text > self.label1.text:
  print("Číslo vpravo je větší")
    elif self.vysledek_label.text == self.label1.text:
  print("Čísla jsou stejná")
    else:
  print("Číslo vpravo je menší")

    def Exit(self,obj):
        #self.stop()
        App.get_running_app().stop()
class MainApp(App):
    def on_stop(self):
        Logger.critical("good bye")
    def build(self):
        return Box()

if __name__ == '__main__':
        MainApp().run()