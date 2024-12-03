from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
import math
from calculation import flight_calculator

class StairCalc(ScreenManager):
    pass


class MainScreen(Screen):
    staircase_height = NumericProperty(0)
    staircase_run = NumericProperty(0)
    stair_max_height = NumericProperty(0)
    stair_min_height = NumericProperty(0)
    stair_max_depth = NumericProperty(0)
    stair_min_depth = NumericProperty(0)
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
        # Validate inputs
        inputs = [
            ("StaircaseHeight", "staircase_height"),
            ("StaircaseDepth", "staircase_run"),
            ("MaxStairHeight", "stair_max_height"),
            ("MinStairHeight", "stair_min_height"),
            ("MaxStairDepth", "stair_max_depth"),
            ("MinStairDepth", "stair_min_depth"),
        ]
        for widget_id, attr in inputs:
            value = self.validate_input(self.ids[widget_id].text)
            if value is None:
                self.ids.MainLabel.text = "Invalid input!"
                self.ids.MainLabel.color = [1, 0, 0, 1]
                return
            setattr(self, attr, value)

        # Calculate solutions
        self.iteration = 0
        self.solutions = flight_calculator(
            self.staircase_height,
            self.staircase_run,
            self.stair_max_height,
            self.stair_min_height,
            self.stair_max_depth,
            self.stair_min_depth,
        )
        if not self.solutions:
            self.ids.MainLabel.text = "No solutions found!"
            self.ids.MainLabel.color = [1, 0, 0, 1]
            return

        # Update the display
        self.hypotenuse = math.sqrt(self.staircase_height ** 2 + self.staircase_run ** 2)
        self.update_solution()

    def next(self):
        """Show the next solution."""
        if not self.solutions:
            return
        self.iteration = (self.iteration + 1) % len(self.solutions)
        self.update_solution()

    def update_solution(self):
        """Update the displayed solution."""
        solution = self.solutions[self.iteration]
        self.ids.Tread_Depth.text = f"{solution[0]:.2f}"
        self.ids.Stair_Height.text = f"{solution[1]:.2f}"
        self.number_of_stairs = round(self.hypotenuse / solution[2], 2)
        self.ids.NumberofStairs.text = f"{self.number_of_stairs}"

    # Additional methods can be added here for future features


class StairCalcApp(App):
    def build(self):
        return StairCalc()


if __name__ == '__main__':
    StairCalcApp().run()
