
def sum_two_numbers(number1, number2):
    if number1 is None or number2 is None:
        raise ValueError("One or both numbers are missing.")
    return number1 + number2


def average_numbers(numbers):
    if len(numbers) == 0:
        return f"The list witch you check is empty!"
    return sum(numbers) / len(numbers)


def sum_even_numbers(numbers):
    if len(numbers) == 0:
        return f"The list witch you check is empty!"

    return sum(number for number in numbers if number % 2 == 0)


def find_unique_value(input_string):
    # The set() function takes a string and creates a set of characters, removing duplicate values.
    unique_value = set(input_string)
    # The len() function returns the number of elements in a set, that is, the number of unique characters in a string.
    unique_count = len(unique_value)

    return unique_count >= 10


