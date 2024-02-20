"""As suggested by Challenge 8.4: Find the Factors of a Number in
Python Basics A Practical Introduction to Python 3
https://realpython.com/products/python-basics-book/"""


def prompt_for_int(prompt_string: str) -> int:
    """Prompts user for input and returns an int"""
    valid_input = False
    input_as_int = 0
    while not valid_input:
        prompt = input(f"{prompt_string}: ")

        try:
            input_as_int = int(prompt)
            valid_input = True
        except ValueError:
            valid_input = False

    return input_as_int


def find_factors(numb: int) -> list:
    """Finds the factors of a number"""
    factors_list = []
    for i in range(1, numb + 1):
        if numb % i == 0:
            factors_list.append(i)

    return factors_list


if __name__ == "__main__":
    number = prompt_for_int("Please enter an integer to find its factors")
    factors = find_factors(number)
    print(f"The factors of {number} are {factors}.")
    print(f"The sum of those factors is {sum(factors)}.")
