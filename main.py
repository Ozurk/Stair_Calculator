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
            self.stairx = 1
            self.stairy = 1
        

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

        # Initial display position
        display_position = (0, 0)

        # Create and position each stair
        for x in range(num_of_stairs):
            stair = Step()  # Assuming Step is a custom widget class
            stair.size_hint = (None, None)  # Disable automatic resizing
            stair.size = (step_width, step_height)  # Set size explicitly
            stair.pos = (display_position[0] + (step_width * x),  # Move right for each stair
                        display_position[1] + (step_height * x))  # Move up for each stair
            full_window.add_widget(stair)

        # Add the full_window to the DisplayScreen (ScrollView)
        screen.add_widget(full_window)

        # Adjust zoom after layout is ready
        def adjust_zoom(*args):
            width_ratio = screen.width / full_window.width
            height_ratio = screen.height / full_window.height
            zoom_out_level = min(width_ratio, height_ratio)  # Choose the smaller ratio for fitting
            screen.scroll_x = 0  # Reset horizontal scroll
            screen.scroll_y = 1  # Reset vertical scroll to the top
            screen.scale = zoom_out_level

        Clock.schedule_once(adjust_zoom, 0.1)



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

