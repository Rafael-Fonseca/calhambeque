from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Carros(BoxLayout):
    def __init__(self, carros, **kwargs):
        super().__init__(**kwargs)

        self.ids.box.add_widget(Logotipo(text='Calhambeque'))
        for carro in carros:
            self.ids.box.add_widget(ItemCarro(text=carro))


class Logotipo(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.logotipo.text = text


class ItemCarro(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label_item_carro.text = text


class Calhambeque(App):
    def build(self):
        return Carros(['Fox', 'Up', 'Gol'])


Calhambeque().run()
