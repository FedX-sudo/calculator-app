import kivy

from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kivy.require('1.9.0')

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '375')
Config.set('graphics', 'resizable', False)

Builder.load_string("""# .kv file implementation of the code
<CustButton@Button>:
    font_size: 32
    size: 75, 75
    size_hint: None, None

<four_function>:
    id: four_function
    padding: None
    spacing: None
    TextInput:
        id: input
        text: ''
        font_size: 32
        multiline: False
        size_hint: None, None
        size: 300, 75
        on_text: app.process("1", 1); output.text+= self.text; input.text = ''
        pos: 0, 300
    Label:
        id: output
        text: ''
        font_size: 32
        color: (0, 0, 0, 1)
        multiline: False
        size_hint: None, None
        size: 300, 75
        pos: 0, 300
    GridLayout:
        cols: 4
        pos: 0, 200
        CustButton:
            text: "7"
            on_press: app.process("7", 2); output.text+= self.text
        CustButton:
            text: "8"
            on_press: app.process("8", 2); output.text+= self.text
        CustButton:
            text: "9"
            on_press: app.process("9", 2); output.text+= self.text
        CustButton:
            text: "+"
            on_press: app.process("+", 2); output.text+= self.text
        CustButton:
            text: "4"
            on_press: app.process("4", 2); output.text+= self.text
        CustButton:
            text: "5"
            on_press: app.process("5", 2); output.text+= self.text
        CustButton:
            text: "6"
            on_press: app.process("6", 2); output.text+= self.text
        CustButton:
            text: "-"
            on_press: app.process("-", 2); output.text+= self.text
        CustButton:
            text: "1"
            on_press: app.process("1", 2); output.text+= self.text
        CustButton:
            text: "2"
            on_press: app.process("2", 2); output.text+= self.text
        CustButton:
            text: "3"
            on_press: app.process("3", 2); output.text+= self.text
        CustButton:
            text: "*"
            on_press: app.process("*", 2); output.text+= self.text
        CustButton:
            text: "ac"
            on_press: app.remove(2); output.text=''
        CustButton:
            text: "="
            on_press: output.text = app.process("1", 4)
        CustButton:
            text: "Del"
            on_press: app.remove(1); output.text = output.text[:-1]
        CustButton:
            text: "Mode"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'id: sci_function'



<sci_function>:
    id: sci_function
    padding: None
    spacing: None
    TextInput:
        id: input
        text: ''
        font_size: 32
        multiline: False
        size_hint: None, None
        size: 300, 75
        on_text: app.process("1", 1); output.text+= self.text; input.text = ''
        pos: 0, 300
    Label:
        id: output
        text: ''
        font_size: 32
        color: (0, 0, 0, 1)
        multiline: False
        size_hint: None, None
        size: 300, 75
        pos: 0, 300
    GridLayout:
        cols: 4
        pos: 0, 200
        CustButton:
            text: "7"
            on_press: app.process("7", 2); output.text+= self.text
        CustButton:
            text: "8"
            on_press: app.process("8", 2); output.text+= self.text
        CustButton:
            text: "9"
            on_press: app.process("9", 2); output.text+= self.text
        CustButton:
            text: "+"
            on_press: app.process("+", 2); output.text+= self.text
        CustButton:
            text: "4"
            on_press: app.process("4", 2); output.text+= self.text
        CustButton:
            text: "5"
            on_press: app.process("5", 2); output.text+= self.text
        CustButton:
            text: "6"
            on_press: app.process("6", 2); output.text+= self.text
        CustButton:
            text: "-"
            on_press: app.process("-", 2); output.text+= self.text
        CustButton:
            text: "1"
            on_press: app.process("1", 2); output.text+= self.text
        CustButton:
            text: "2"
            on_press: app.process("2", 2); output.text+= self.text
        CustButton:
            text: "3"
            on_press: app.process("3", 2); output.text+= self.text
        CustButton:
            text: "*"
            on_press: app.process("*", 2); output.text+= self.text
        CustButton:
            text: "ac"
            on_press: app.remove(2); output.text=''
        CustButton:
            text: "="
            on_press: output.text = app.process("1", 4)
        CustButton:
            text: "Del"
            on_press: app.remove(1); output.text = output.text[:-1]
        CustButton:
            text: "Mode"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'four_function'


""")


class four_function(Screen):
    pass


class sci_function(Screen):
    pass


# Building text input
screen_manager = ScreenManager()

screen_manager.add_widget(four_function(name="four_function"))
screen_manager.add_widget(sci_function(name="sci_function"))


def remove(rmtype):
    global text_inp
    if rmtype == 1:
        text_inp = text_inp[:-1]
    if rmtype == 2:
        text_inp = ''

class MainApp(App):
    global text_inp

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = None
        super().__getattr__ = super.__getattribute__(**kwargs)

    def process(self, num, type1):
        global text_inp
        if type1 == 1:
            if self.text == "return":
                self.process('1', 4)
            else:
                text_inp += self.root.ids.input.text

        elif type1 == 2:
            text_inp += num
        else:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                return str(eval(text_inp))
            except Exception:
                return "Error"

    def build(self):
        return screen_manager

text_inp = ''
# Run the App
if __name__ == "__main__":
    MainApp().run()
