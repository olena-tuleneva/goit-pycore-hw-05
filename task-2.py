
import re
from typing import Callable, Generator

# Генератор для вилучення чисел з тексту
def generator_numbers(text: str) -> Generator[float, None, None]: # Генератор дійсних чисел
    pattern = r'\b\d+(?:\.\d+)?\b' # Регулярний вираз для ідентифікації дійсних чисел

    for match in re.findall(pattern, text): # Пошук всіх збігів
        yield float(match) # Повернення числа як float

# Функція для обчислення суми прибутку, яка використовує генератор як аргумент
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
       return sum(func(text)) 


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")