from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label  import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
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

    solutions = []

    def submit(self):
        self.staircase_height = float(self.ids.StaircaseHeight.text)
        self.staircase_run = float(self.ids.StaircaseDepth.text)
        self.stair_max_height = float(self.ids.MaxStairHeight.text)
        self.stair_min_height = float(self.ids.MinStairHeight.text)
        self.stair_max_depth = float(self.ids.MaxStairDepth.text)
        self.stair_min_depth = float(self.ids.MinStairDepth.text)

        self.solutions = flight_calculator(self.staircase_height,self.staircase_run, self.stair_max_height, self.stair_min_height, self.stair_max_depth, self.stair_min_depth)

        # --- Validation Here ---

        print(flight_calculator(self.staircase_height,self.staircase_run, self.stair_max_height, self.stair_min_height, self.stair_max_depth, self.stair_min_depth))





class StairCalcApp(App):
    def build(self):
        app = StairCalc()
        return app

def flight_calculator(rise_of_fight, run_of_flight, stair_max_height, stair_min_height, stair_max_run, stair_min_run):
    hypotenuse_of_flight = math.sqrt(rise_of_fight ** 2 + run_of_flight ** 2)
    solutions = []
    stair_height_list = generate_tenths(stair_min_height, stair_max_height)
    stair_depth_list = generate_tenths(stair_min_run, stair_max_run)
    flight_triangle = [rise_of_fight, run_of_flight, hypotenuse_of_flight]

    small_triangle_list = small_trangle_maker(stair_height_list, stair_depth_list)
    for triangle in small_triangle_list:
        result = big_triangle_tester(flight_triangle, triangle)
        if result is not None:  # Filter out None values
            solutions.append(result)

    # Convert solutions to DataFrame and write to CSV
    df = pd.DataFrame(solutions, columns=["rise", "run", "hypotenuse"])
    df.to_csv("solutions.csv", index=False)  # Save to CSV without row indices
    return solutions


def big_triangle_tester(big_triangle, little_triangle):
    modulo = big_triangle[2] % little_triangle[2]
    if modulo < .5:
        return little_triangle
        

def small_trangle_maker(height_list, length_list):
    small_triangles = []
    for height in height_list:
        for length in length_list:
            small_triangles.append(triangle_validator(height, length))
    return small_triangles


def triangle_validator(rise, run):
    hypotenuse = math.sqrt(rise ** 2 + run ** 2)
    try:
        a = math.atan(rise / run)
    except ZeroDivisionError:
        return "Tread Depth is Zero"
    try:
        b = math.atan(run / rise)
    except ZeroDivisionError:
        "Rise is Zero"
    valid = [rise, run, hypotenuse]
    if valid == None:
        pass
    return valid
        



def generate_tenths(start, end):
    return [round(x, 1) for x in frange(start, end, 0.1)]

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step








if __name__ == '__main__':
    app = StairCalcApp()
    app.run()

