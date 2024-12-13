from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
import math
from calculation import flight_calculator # Rename this 
from calculation import flight_calc
from kivy.base import Builder
Builder.load_file("StairCalc.kv")
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
from time import sleep


# LabelBase.register(name="fonts/cambria.ttc", fn_regular="fonts/cambria.ttc", fn_bold="fonts/cambriab.ttf")


class StairCalc(ScreenManager):
    pass


class StairSize(Screen):
    staircase_height = NumericProperty(0)
    staircase_run = NumericProperty(0)
    number_of_stairs = NumericProperty(0)
    hypotenuse = NumericProperty(0)
    iteration = NumericProperty(0)

    solutions = []

    def validate_input(self, value):
        """Validate numeric input."""
        try:
            return float(value)
        except ValueError:
            return None

    def submit(self):
        try:
            self.staircase_run = float(self.ids.StairCaseX.text)
            self.staircase_height = float(self.ids.StairCaseY.text)
            self.number_of_stairs = int(self.ids.NumberofStairs.text)
        except ValueError:
            self.staircase_run = 100
            self.staircase_height = 100
            self.number_of_stairs = 20
        

        self.build_staircase(self.number_of_stairs)

    def build_staircase(self, num_of_stairs):
        # get displayscreen [where the stair graphics will be built]
        screen = self.ids.DisplayScreen
        screen.clear_widgets()
        # calculate Stair width
        step_width = screen.width / num_of_stairs
        step_height = screen.height / num_of_stairs
        display_position = screen.pos
        for x in range(num_of_stairs):
            print(x)
            stair = Step()
            stair.size = (step_width, step_height)
            stair.pos = (display_position[0] + (step_width * x)), (display_position[1] + (step_height * x))
            screen.add_widget(stair)


class StartScreen(Screen):
    pass

class Step(Widget):
    pass


class Flight_Calculator(Screen):
    flight_height = NumericProperty
    flight_depth = NumericProperty
    stair_height = NumericProperty
    stair_depth = NumericProperty
    number_of_stairs = NumericProperty()
    def calculate(self):
        try:
            self.flight_height = float(self.ids.Flight_Height.text)
            self.stair_height = float(self.ids.Stair_Height.text)
            self.stair_depth = float(self.ids.Stair_Depth.text)
            self.flight_depth = round(float(flight_calc(self.flight_height, self. stair_height, self.stair_depth)), 2)
            self.ids.CalcDepth.text = str(self.flight_depth)
            self.ids.WarningLabel.text = ""
        except ValueError:
            self.ids.WarningLabel.text = "Invalid Input"
            self.ids.WarningLabel.color = (1, 0, 0, 1)
        except ZeroDivisionError:
            self.ids.WarningLabel.text = "Cannot Divide by Zero"
            # self.build_staircase(self.number_of_stairs, self.flight_depth, self.flight_height)
            self.build_staircase(5, 200, 100)

    def build_staircase(self, num_of_stairs, staircase_x, staircase_y):
        # get displayscreen [where the stair graphics will be built]
        screen = self.ids.DisplayScreen
        # calculate Stair width
        step_width = screen.width / num_of_stairs
        step_height = screen.height / num_of_stairs
        display_position = screen.pos
        for stair in range(num_of_stairs):
            print(stair)
            stair = Step()
            stair.size = (step_width, step_height)
            stair.pos = (display_position + (step_width * stair)), (display_position + (step_height * stair))

            
            

        
class DisplayScreen(Widget):
    pass



class StairCalcApp(App):
    def build(self):
        return StairCalc()


if __name__ == '__main__':
    StairCalcApp().run()

