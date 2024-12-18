import math


def flight_calculator(rise_of_flight, run_of_flight,):
    # Calculate the hypotenuse of the full staircase
    hypotenuse_of_flight = math.sqrt(rise_of_flight ** 2 + run_of_flight ** 2)
    try:
        flight_angle = math.atan((rise_of_flight / run_of_flight))
    except ZeroDivisionError:
        flight_angle = 00000000
    flight_angle = flight_angle * (180 / math.pi)
    flight_angle = round(flight_angle, 2)
    return hypotenuse_of_flight, flight_angle

def flight_calc(flight_height, stair_height, stair_depth):
    number_of_stairs = flight_height / stair_height
    staircase_depth = stair_depth * number_of_stairs
    return staircase_depth