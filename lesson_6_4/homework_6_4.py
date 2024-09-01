# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6]

sum_numbers = sum(number for number in numbers if number % 2 == 0)
print(f"Sum of even numbers = {sum_numbers}")
