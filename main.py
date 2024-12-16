from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
import math
from calculation import flight_calculator # Rename this 
from calculation import flight_calc
from kivy.base import Builder
# Builder.load_file("StairCalc.kv")
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
from time import sleep
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock


# LabelBase.register(name="fonts/cambria.ttc", fn_regular="fonts/cambria.ttc", fn_bold="fonts/cambriab.ttf")


class StairCalc(ScreenManager):
    pass


class StairSize(Screen):
    staircase_height = NumericProperty(0)
    staircase_run = NumericProperty(0)
    number_of_stairs = NumericProperty(0)
    hypotenuse = NumericProperty(0)
    iteration = NumericProperty(0)
    stairx = NumericProperty(0)
    stairy = NumericProperty(0)

    solutions = []

    def validate_input(self, value):
        """Validate numeric input."""
        try:
            return float(value)
        except ValueError:
            return None

    def submit(self):
        try:
            # self.staircase_run = float(self.ids.StairCaseX.text)
            # self.staircase_height = float(self.ids.StairCaseY.text)
            self.number_of_stairs = int(self.ids.NumberofStairs.text)
            self.stairx = float(self.ids.StairX.text)
            self.stairy = float(self.ids.StairY.text)
        except ValueError:
            self.staircase_run = 100
            self.staircase_height = 100
            self.number_of_stairs = 20
            self.stairx = 11
            self.stairy = 9
        

        self.build_staircase(self.number_of_stairs, self.stairx, self.stairy)

    def build_staircase(self, num_of_stairs, stair_x, stair_y):
        # Get the DisplayScreen, which is a ScrollView
        screen = self.ids.DisplayScreen
        screen.clear_widgets()  # Clear previous content

    # Create a container (RelativeLayout) for the stairs
        full_window = RelativeLayout(size_hint=(None, None))

    # Calculate stair width and height
        step_width = stair_x * 10
        step_height = stair_y * 10

    # Dynamically set the size of the full_window to fit all stairs
        full_window.width = step_width * num_of_stairs
        full_window.height = step_height * num_of_stairs

    # Check if the stairs go off-screen and resize if necessary
        max_width = screen.width
        max_height = screen.height
        print(screen.width)

        if full_window.width > max_width or full_window.height > max_height:
            scale_factor = min(max_width / full_window.width, max_height / full_window.height)
            step_width *= scale_factor
            step_height *= scale_factor

    # Update the full_window dimensions after scaling
        full_window.width = step_width * num_of_stairs
        full_window.height = step_height * num_of_stairs

    # Initial display position
        display_position = (0, 0)


    # Create and position each stair
        for columns in range(num_of_stairs):
            for stairs in range(columns):
                stair = Step(size_hint=(None, None))
                stair.size = (step_width, step_height)
                stair.pos = (display_position[0] + (stair.width * columns), display_position[1] + (stair.height * stairs))
                full_window.add_widget(stair)

    # Add the full_window to the DisplayScreen (ScrollView)
        screen.add_widget(full_window)



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



class StairCalcApp(App):
    def build(self):
        return StairCalc()


if __name__ == '__main__':
    StairCalcApp().run()

