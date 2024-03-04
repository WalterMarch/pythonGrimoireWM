""" As suggested by Challenge 6.5: Track Your Investments in
Python Basics A Practical Introduction to Python 3
https://realpython.com/products/python-basics-book/"""


def prompt_for_float(prompt_string: str) -> float:
    """Prompts user for input and returns a float"""
    valid_input = False
    input_as_float = 0.0
    while not valid_input:
        prompt = input(f"{prompt_string}: ")

        try:
            input_as_float = float(prompt)
            valid_input = True
        except ValueError:
            valid_input = False

    return input_as_float


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


def invest(amount: float, rate: float, years: int) -> None:
    """Simulates an investment over time"""
    print(f"Investing {amount} at {rate} for {years} years...")

    for i in range(years):
        amount += amount * rate
        print(f"year {i+1}: {amount:,.2f}")


if __name__ == "__main__":
    initial_investment = prompt_for_float(
        "Enter dollar amount (number only) of initial investment"
    )
    rate_of_return = prompt_for_float(
        "Enter percentage rate of return as a decimal number"
    )
    years_of_investment = prompt_for_int("Enter number of years to simulate")

    invest(initial_investment, rate_of_return, years_of_investment)
