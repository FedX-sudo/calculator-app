import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

kivy.require('1.9.0')

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '375')
Config.set('graphics', 'resizable', False)


class textinp(Widget):
    pass


def entry():
    return text_inp


# Building text input


class MainApp(App):
    global text_inp

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = None

    def build(self):
        return textinp()

    @property
    def entry(self):
        return text_inp

    def remove(self, rmtype):
        global text_inp
        if rmtype == 1:
            text_inp = text_inp[:-1]
        if rmtype == 2:
            text_inp = ''


    def process(self, num, type1):
        global text_inp
        if type1 == 1:
            if self.text == "return":
                self.process('1', 4)

        elif type1 == 2:
            text_inp += num
        else:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                return str(eval(text_inp))
            except Exception:
                return "Error"
        print(text_inp)


text_inp = ''
# Run the App
if __name__ == "__main__":
    MainApp().run()