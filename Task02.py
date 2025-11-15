import re
from typing import Callable, Generator


def generator_numbers(text: str):
                                      # Pattern to match integers and floats
    pattern = r' (\d+(?:\.\d+)?) '
                                      # Find all matches in the text
    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, num):
                                       # Summing up all numbers generated
    return sum(num(text))


text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
)
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
