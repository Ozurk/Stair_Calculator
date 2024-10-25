from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label  import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import math


    
class StairCalc(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class StairCalcApp(App):
    def build(self):
        app = StairCalc()
        return app

def flight_calculator(rise_of_fight, run_of_flight, stair_max_height, stair_min_height, stair_max_run, stair_min_run):
    hypotenuse_of_flight = math.sqrt(rise_of_fight ** 2 + run_of_flight ** 2)


def triangle_validator(rise, run):
    hypotenuse = math.sqrt(rise ** 2 + run ** 2)
    try:
        A = math.atan(rise / run)
    except ZeroDivisionError:
        return "Tread Depth is Zero"
    try:
        B = math.atan(run / rise)
    except ZeroDivisionError:
        "Rise is Zero"
    return {'Angles': [math.pi / 2, A, B], "Sides": [rise, run, hypotenuse]}
        

x =triangle_validator(12.1, 6)
print(x)
if __name__ == '__main__':
    app = StairCalcApp()
   # app.run()
