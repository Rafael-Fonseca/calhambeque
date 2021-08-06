from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from back_or_next import BtBackOrNext
from logotype import LogotipoVertical


class ScNewCar(Screen):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.sm = sm
        self.name = 'ScNewCar'

    def plot_me(self):
        base = GridLayout(rows=6)
        base.add_widget(LogotipoVertical())
        base.add_widget(BoxInputText('Apelido:').plot_me())
        base.add_widget(BoxInputText('Marca:').plot_me())
        base.add_widget(BoxInputText('Modelo:').plot_me())
        base.add_widget(BoxInputText('Ano de Fabricação:').plot_me())
        base.add_widget(BtBackOrNext(self.sm, 'ScMyCars', 'Voltar', 'Adicionar', 'ScMyCars'))

        self.add_widget(base)
        return self


class BoxInputText:
    def __init__(self, text, font_size=20, size=(0, 50), size_hint=(1, None)):
        self.text = text
        self.font_size = font_size
        self.size = size
        self.size_hint = size_hint

    def plot_me(self):
        panel = BoxLayout(size_hint=self.size_hint, size=self.size)
        panel.add_widget(Label(text=self.text, font_size=self.font_size))
        panel.add_widget(TextInput())
        return panel



