import math
import pandas as pd


def flight_calculator(rise_of_flight, run_of_flight, stair_max_height, stair_min_height, stair_max_run, stair_min_run, csv_file="solutions.csv"):
    # Calculate the hypotenuse of the full staircase
    hypotenuse_of_flight = math.sqrt(rise_of_flight ** 2 + run_of_flight ** 2)
    flight_triangle = (rise_of_flight, run_of_flight, hypotenuse_of_flight)
    
    # Generate potential stair dimensions
    stair_heights = generate_tenths(stair_min_height, stair_max_height)
    stair_runs = generate_tenths(stair_min_run, stair_max_run)
    
    # Filter and validate solutions
    solutions = [
        triangle for triangle in generate_triangles(stair_heights, stair_runs)
        if big_triangle_tester(flight_triangle, triangle)
    ]
    
    # Save solutions to CSV
    pd.DataFrame(solutions, columns=["rise", "run", "hypotenuse"]).to_csv(csv_file, index=False)
    return solutions


def big_triangle_tester(big_triangle, little_triangle):
    # Check if the hypotenuse of the big triangle is divisible by the small triangle's hypotenuse
    return math.isclose(big_triangle[2] % little_triangle[2], 0, abs_tol=0.1)


def generate_triangles(heights, runs):
    # Generate all valid triangles given lists of heights and runs
    return (
        (rise, run, math.sqrt(rise ** 2 + run ** 2))
        for rise in heights for run in runs
    )


def generate_tenths(start, end):
    # Generate values with a step of 0.1
    return [round(x, 1) for x in frange(start, end, 0.1)]


def frange(start, stop, step):
    # Floating-point range generator
    while start <= stop:
        yield start
        start += step

def flight_calc(flight_height, stair_height, stair_depth):
    number_of_stairs = flight_height / stair_height
    staircase_depth = stair_depth * number_of_stairs
    return staircase_depth