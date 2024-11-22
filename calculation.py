import math
import pandas as pd


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
    if modulo < .1:
        return little_triangle
            

def small_trangle_maker(height_list, length_list):
        small_triangles = [triangle_validator(height, length) for height in height_list for length in length_list]
        return small_triangles


def triangle_validator(rise, run):
        if run == 0:
            return "Tread Depth is Zero"
        if rise == 0:
            return "Rise is Zero"
        hypotenuse = math.sqrt(rise ** 2 + run ** 2)
        return [rise, run, hypotenuse]

        



def generate_tenths(start, end):
    return [round(x, 1) for x in frange(start, end, 0.1)]

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step