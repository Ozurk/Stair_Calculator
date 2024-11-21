from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label  import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from StairCalc import Flight_Calculator
import math
import pandas as pd
import os

    
class StairCalc(ScreenManager):
    pass

class MainScreen(Screen):
    staircase_height = None
    staircase_run = None
    stair_max_height = None
    stair_min_height = None
    stair_max_depth = None
    stair_min_depth = None
    number_of_stairs = None
    hypotenuse = None
    iteration = 0

    solutions = []
    example_triangle = []

    def submit(self):
        self.iteration = 0
        self.staircase_height = float(self.ids.StaircaseHeight.text)
        self.staircase_run = float(self.ids.StaircaseDepth.text)
        self.stair_max_height = float(self.ids.MaxStairHeight.text)
        self.stair_min_height = float(self.ids.MinStairHeight.text)
        self.stair_max_depth = float(self.ids.MaxStairDepth.text)
        self.stair_min_depth = float(self.ids.MinStairDepth.text)

        self.solutions = StairCalc.flight_calculator(self.staircase_height,self.staircase_run, self.stair_max_height, self.stair_min_height, self.stair_max_depth, self.stair_min_depth)
        self.ids.Tread_Depth.text = str(self.solutions[0][0])
        self.ids.Stair_Height.text = str(self.solutions[0][1])
        self.hypotenuse = math.sqrt((self.staircase_height ** 2) + (self.staircase_run ** 2))
        self.number_of_stairs = round((self.hypotenuse / self.solutions[0][2]),2)
        self.ids.NumberofStairs.text = str(self.number_of_stairs)

        print(self.solutions[0][2])
        print(self.hypotenuse)
    
    def next(self):
        try:
            if self.iteration + 1 < len(self.solutions):
                self.iteration += 1
            else:
                self.iteration = 0
            self.solutions = Flight_Calculator.flight_calculator(self.staircase_height,self.staircase_run, self.stair_max_height, self.stair_min_height, self.stair_max_depth, self.stair_min_depth)
            self.ids.Tread_Depth.text = str(self.solutions[self.iteration][0])
            self.ids.Stair_Height.text = str(self.solutions[self.iteration][1])
            self.hypotenuse = math.sqrt((self.staircase_height ** 2) + (self.staircase_run ** 2))
            self.number_of_stairs = round((self.hypotenuse / self.solutions[self.iteration][2]), 2)
            self.ids.NumberofStairs.text = str(self.number_of_stairs)
        except IndexError:
            self.iteration = 0

        print(self.solutions[self.iteration][2])
        print(self.hypotenuse)
        print(self.iteration)
        
        



        # --- Validation Here ---



class StairCalcApp(App):
    def build(self):
        app = StairCalc()
        return app









if __name__ == '__main__':
    app = StairCalcApp()
    app.run()

