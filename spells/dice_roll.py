"""As suggested by Review Exercises on p 227
Python Basics A Practical Introduction to Python 3
https://realpython.com/products/python-basics-book/"""

from random import randint


def roll_dice(num_of_dice: int, num_of_sides: int) -> list:
    """Simulates rolling a number of dice with a number of sides"""
    rolls_list = []
    for _ in range(num_of_dice):
        rolls_list.append(randint(1, num_of_sides))

    return rolls_list


def prompt_for_positive_int(prompt_string: str) -> int:
    """Prompts user for input and returns a positive int"""
    valid_input = False
    input_as_int = 0
    while not valid_input:
        response = input(f"{prompt_string}: ")

        try:
            input_as_int = int(response)
            if input_as_int < 1:
                valid_input = False
            else:
                valid_input = True
        except ValueError:
            valid_input = False

    return input_as_int


if __name__ == "__main__":
    number_of_dice = prompt_for_positive_int("How many dice would you like to roll?")
    number_of_sides = prompt_for_positive_int("How many sides should each die have?")
    rolls = roll_dice(number_of_dice, number_of_sides)
    print(f"You rolled {rolls}.")
    total = sum(rolls)
    print(f"The sum of those rolls is {total}.")
    print(f"The average of those rolls is {total / number_of_dice}.")
