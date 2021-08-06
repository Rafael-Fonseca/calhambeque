from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class LogotipoVertical(BoxLayout):
    def __init__(self, height=100, text='Calhambeque', font_size=30, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = height
        self.add_widget(Label(text=text, font_size=font_size))
