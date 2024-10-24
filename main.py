from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label  import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


    
class StairCalc(ScreenManager):
    pass



class MainScreen(Screen):
    pass


class StairCalcApp(App):
    def build(self):
        app = StairCalc()
        return app


if __name__ == '__main__':
    app = StairCalcApp()
    app.run()
