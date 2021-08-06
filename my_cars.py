from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from logotype import LogotipoVertical
from new_car import ScNewCar
from utils import FileUtils


class Field(GridLayout):
    def __init__(self, name, bg):
        self.bg = bg
        GridLayout.__init__(self,
                            rows=1,
                            padding=10,
                            size=(0, 60),
                            size_hint=(1, None))
        self.add_widget(Label(text=name))
        self.add_widget(Button(text='X',
                               size=(60, 0),
                               size_hint=(None, 1)))
        self.bind(pos=self.change_background)
        self.bind(size=self.change_background)

    def change_background(self, *args):  # Se apagar o *args dá erro.
        self.canvas.before.clear()
        with self.canvas.before:
            if self.bg:
                Color(0.2, 0.2, 0.2, mode='rgb')
            else:
                Color(0.1, 0.1, 0.1, mode='rgb')
            Rectangle(pos=self.pos, size=self.size)


class CarSpace:
    def __init__(self, path):
        self.path = path
        self.utils = FileUtils()

    def plot_cars(self):
        cars_space = ScrollView()
        cars_space.view = GridLayout(cols=1, size_hint=(1, None))
        cars_space.add_widget(cars_space.view)
        cars_space.view.bind(minimum_height=cars_space.view.setter('height'))  # Mantem a tela ao soltar o scroll

        cars = self.utils.load_data(self.path + 'data.json')
        # print('cars', '\t', cars)
        _ = 0
        for car in cars:
            # print('car', '\t', car)
            cars_space.view.add_widget(Field(car.get('Apelido:'), _ % 2 == 0))
            _ += 1
        return cars_space


class NewCar(BoxLayout):
    def __init__(self,
                 sm,
                 size=(0, 60),
                 size_hint=(1, None),
                 text='Novo Carro',
                 font_size=30,
                 **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.size_hint = size_hint
        self.sm = sm
        self.add_widget(Button(text=text, font_size=font_size,
                               on_release=self.change_screen
                               ))

    def change_screen(self, *args):
        # Se retirar o args dá problema, uma vez que o kivy utiliza argumentos para chamar o on_release
        self.sm.current = 'ScNewCar'


class ScMyCars(Screen):
    def __init__(self, sm, path, **kwargs):
        super().__init__(**kwargs)
        self.name = 'ScMyCars'
        self.sm = sm
        self.path = path
        self.cars = CarSpace(self.path).plot_cars()

    def on_pre_enter(self):
        self.cars = CarSpace(self.path).plot_cars()
        self.plot_me()

    def plot_me(self):
        base = GridLayout(rows=3)
        base.add_widget(LogotipoVertical())
        base.add_widget(self.cars)
        base.add_widget(NewCar(self.sm))
        self.add_widget(base)
        return self


class Calhambeque(App):
    def build(self):
        path = App.get_running_app().user_data_dir + '/'
        sm = ScreenManager()
        sm.add_widget(ScMyCars(sm, path).plot_me())
        sm.add_widget(ScNewCar(sm, path).plot_me())
        return sm


Calhambeque().run()
