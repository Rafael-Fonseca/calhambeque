from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BtBackOrNext(BoxLayout):
    def __init__(self,
                 sm,
                 screen_name_back,
                 text_back,
                 text_next,
                 screen_name_next,
                 function_next=None,
                 size=(0, 60),
                 size_hint=(1, None),
                 font_size=30,
                 spacing=10,
                 padding=10,
                 **kwargs):

        super().__init__(**kwargs)
        self.sm = sm
        self.screen_name_back = screen_name_back
        self.screen_name_next = screen_name_next
        self.function_next = function_next
        self.size = size
        self.size_hint = size_hint
        self.spacing = spacing
        self.padding = padding
        self.add_widget(Button(text=text_back, font_size=font_size,
                               on_release=self.go_back))
        self.add_widget(Button(text=text_next, font_size=font_size,
                               on_release=self.go_next))


    def go_back(self, *args):
        # Se retirar o args dá problema, uma vez que o kivy utiliza argumentos para chamar o on_release
        self.sm.current = self.screen_name_back

    def go_next(self, *args):
        # Se retirar o args dá problema, uma vez que o kivy utiliza argumentos para chamar o on_release
        if self.function_next is not None:
            self.function_next()
            self.sm.current = self.screen_name_next
        self.sm.current = self.screen_name_next
