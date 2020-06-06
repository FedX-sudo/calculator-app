import kivy
# import the python code
import four_function
import sci_functoin
import multiprocessing

kivy.require('1.9.0')

if __name__ == "__main__":
    four_function.MainApp().run()

def run(num):
    if num == 1:
        four_function.MainApp().run()
    if num == 2:
        four_function.MainApp().stop()
        r = multiprocessing.Process(target=sci_functoin.MainApp.run(self))
        r.start(self)
