from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager


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


class LogotipoVertical(BoxLayout):
    def __init__(self, height=100, text='Calhambeque', font_size=30, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = height
        self.add_widget(Label(text=text, font_size=font_size))


class NewCar(BoxLayout):
    def __init__(self,
                 size=(0, 60),
                 size_hint=(1, None),
                 text='Novo Carro',
                 font_size=30,
                 **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.size_hint = size_hint
        self.add_widget(Button(text=text, font_size=font_size
                               #on_release > Chama Screen Add Car
                               ))


class MyCars:
    base = GridLayout(rows=3)

    '''*******************************
    **      ESPAÇO DOS CARROS      ***
    *******************************'''
    karts = ['1', '2', '3']

    cars_space = ScrollView()
    cars_space.view = GridLayout(cols=1, size_hint=(1, None))
    cars_space.add_widget(cars_space.view)
    cars_space.view.bind(minimum_height=cars_space.view.setter('height'))
    _ = 0
    for kart in karts:
        cars_space.view.add_widget(Field(kart, _ % 2 == 0))
        _ += 1

    base.add_widget(LogotipoVertical())
    base.add_widget(cars_space)
    base.add_widget(NewCar())

    home = Screen(name='home')
    home.add_widget(base)


class Calhambeque(App):
    def build(self):
        sm = ScreenManager()
        home = MyCars()
        sm.add_widget(home.home)
        return sm


Calhambeque().run()
