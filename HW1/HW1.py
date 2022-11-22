from random import random
import logging

from HW1.convert import convert
from HW1.future import future


def function1():
    """Play with output statements, similar to slide #28 of Part 1"""
    print("Hi this is a test")


def function2():
    """Play with variables, similar to slide #19 of Part 1"""
    fstring: str = "fstrings"
    print(f"Hi this is a test using variables and {fstring}")


def function3():
    """Play with expressions, similar to slide #24 of Part 1"""
    num1: float = random()
    num2: float = random()
    print(
        f"Hi this is messing with adding expressions!\n{num1:3f} + {num2:3f} = {num1+num2:3f}"
    )


def function4():
    """Play with assignment statements, similar to slide #7-8 of Part 2"""
    my_weight_lbs: int = 135
    my_weight_grams: int = my_weight_lbs * 0.002205
    print(f"My weight in grams is: {my_weight_grams}")


if __name__ == "__main__":
    function1()
    function2()
    function3()
    function4()
    # Run convert.py program as in slide #11 of Part 3 but with different numbers.
    convert()
    logging.warning(
        "NEVER USE EVAL IN THIS WAY\nWHOEVER WROTE THIS DOES NOT KNOW HOW TO PROGRAM\nRUNNING EVAL FROM UNSANITIZED INPUT MEANS THE PROGRAM WILL RUN WHATEVER I PUT IN"
    )
    # Run futval.py program as in slide #21 of Part 3 but with different numbers.
    future()
    logging.warning(
        "NEVER USE EVAL IN THIS WAY\nWHOEVER WROTE THIS DOES NOT KNOW HOW TO PROGRAM"
    )
