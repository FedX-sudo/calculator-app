import kivy

from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kivy.require('1.9.0')

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '375')
Config.set('graphics', 'resizable', False)

class four_function(Screen):
    pass

class sci_function(Screen):
    pass


# Building text input


class MainApp(App):
    input_text = ObjectProperty(None)
    Builder.load_file('main.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = None

    def build(self):
        return screen_manager

    @staticmethod
    def remove(rmtype):
        global input_text
        if rmtype == 1:
            input_text = input_text[:-1]
        if rmtype == 2:
            input_text = ''

    def process(self, num, type1):
        global input_text
        if type1 == 1:
            if self.text == "return":
                self.process('1', 4)
            else:
                input_text += self.root.ids.input.text

        elif type1 == 2:
            input_text += num
        else:
            try:
                return str(eval(input_text))
            except Exception:
                return "Error"


screen_manager = ScreenManager()

screen_manager.add_widget(four_function(name="four_function"))
screen_manager.add_widget(sci_function(name="sci_function"))



input_text = ''
# Run the App
if __name__ == "__main__":
    MainApp().run()
