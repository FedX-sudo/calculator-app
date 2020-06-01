from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):
    # layout
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display = None
        self.lbl1 = Label(text="test")
        self.txt1 = TextInput(text='', multiline=False)

    def build(self):

        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        layout.add_widget(self.lbl1)
        layout.add_widget(self.txt1)
        return layout

    # button click function
    def buttonClicked(self, btn):
        self.display.text = str(eval())


# run app
if __name__ == "__main__":
    MyApp().run()
# join all items in a list into 1 big string
