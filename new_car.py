from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from back_or_next import BtBackOrNext
from logotype import LogotipoVertical
from utils import FileUtils


class BoxInputText:
    def __init__(self, text, font_size=20, size=(0, 35), size_hint=(1, None)):
        self.text = text
        self.font_size = font_size
        self.size = size
        self.size_hint = size_hint

        self.label = Label(text=self.text, font_size=self.font_size)
        self.text_input = TextInput()

    def plot_me(self):
        panel = BoxLayout(size_hint=self.size_hint, size=self.size)
        panel.add_widget(self.label)
        panel.add_widget(self.text_input)
        return panel


def clear_fields(*args):
    for _ in args:
        _.text_input.text = ''


class ScNewCar(Screen):
    def __init__(self, sm, path, **kwargs):
        super().__init__(**kwargs)
        self.name = 'ScNewCar'
        self.sm = sm
        self.path = path
        self.utils = FileUtils()

        self.apelido = BoxInputText('Apelido:')
        self.marca = BoxInputText('Marca:')
        self.modelo = BoxInputText('Modelo:')
        self.ano = BoxInputText('Ano de Fabricação:')

    def add_car(self):
        car_data = self.prepare_car_data()
        clear_fields(self.apelido, self.marca, self.modelo, self.ano)
        self.utils.save_data(self.path + 'data.json', car_data)

    def prepare_car_data(self):
        car_data = {}
        keys = [self.apelido.text, self.marca.text,
                self.modelo.text,  self.ano.text]
        values = [self.apelido.text_input.text, self.marca.text_input.text,
                  self.modelo.text_input.text,  self.ano.text_input.text]

        for _ in range(0, len(keys)):
            car_data.update({keys[_]: values[_]})
        return car_data

    def plot_me(self):
        base = GridLayout(rows=6)
        base.add_widget(LogotipoVertical())
        base.add_widget(self.apelido.plot_me())
        base.add_widget(self.marca.plot_me())
        base.add_widget(self.modelo.plot_me())
        base.add_widget(self.ano.plot_me())
        base.add_widget(BtBackOrNext(self.sm, 'ScMyCars', 'Voltar', 'Adicionar', 'ScMyCars', self.add_car))
        self.add_widget(base)
        return self
