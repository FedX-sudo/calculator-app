# Program to Show how to use textinput
# (UX widget) in kivy using .kv file

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
from kivy.uix.widget import Widget

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')


# Widgets are elements
# of a graphical user interface
# that form part of the User Experience.


# The TextInput widget provides a
# box for editable plain text

# This layout allows you to set relative coordinates for children.


# Create the widget class
class textinp(Widget):
    pass


# Create the app class


class MainApp(App):
    # Building text input
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = None

    def build(self):
        return textinp()

    # Arranging that what you write will be shown to you
    # in IDLE
    def process(self, num, type1):
        global text
        if type1 == 1:
            if self.text == "enter":
                self.process('1', 4)
            text = self.root.ids.input.text

        elif type1 == 2:
            text += num
        elif type1 == 3:
            text = ""
        else:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                print(str(eval(text)))
            except Exception:
                print("Error")
        print(text)


# Run the App
if __name__ == "__main__":
    MainApp().run()
