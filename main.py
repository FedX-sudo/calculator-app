import kivy
# import the python code
import four_function
import sci_functoin

kivy.require('1.9.0')


def run(num):
    if __name__ == "__main__":
        if num == 1:
            four_function.MainApp().run()
        if num == 2:
            sci_functoin.MainApp().run()


run(1)
