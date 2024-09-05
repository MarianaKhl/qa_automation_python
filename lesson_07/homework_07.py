# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result <= 25:
            print(f"{number} x {multiplier} = {result}")
            multiplier += 1
        else:
            break

multiplication_table(3)

print("#" * 100)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def result_sum(number1, number2):
    sum = number1 + number2
    print(sum)
result_sum(10, 12)

print("#" * 100)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def result_average(numbers):
    if len(numbers) == 0:
        return f"The list is empty"

    average_result = sum(numbers) / len(numbers)
    print(average_result)

numbers = [1, 6, 33]
result_average(numbers)

print("#" * 100)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def vice_versa_result(sentence):
    if len(sentence) == 0:
        return f"The sentence is empty"

    reverce_line = sentence[::-1]
    print(f"Reversed result: {reverce_line}")

sentance = "Hi! How are you?"
vice_versa_result(sentance)

print("#" * 100)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def long_word(sentance):
    if len(sentance) == 0:
        return f"The sentence are absent"
    words = sentance.split()   # is the list of words obtained after splitting the sentence with split()
    longest_word = max(words, key=len)   # calculates the length of each word
    print(longest_word)

sentance = "This is a simple sentence with several words"
long_word(sentance)
print("#" * 100)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    if str2 in str1:
        return 7
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

print("#" * 100)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
""""  Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""
def sum_for_even_numbers(numbers):
    if len(numbers) == 0:
        return f"The list is empty"

    sum_numbers = sum(number for number in numbers if number % 2 == 0)
    print(f"Sum of even numbers = {sum_numbers}")

numbers = [3, 4, 5, 6]
sum_for_even_numbers(numbers)

print("#" * 100)

# task 8
""""" Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими
"""

def creator_string_list(list1):
    if len(list1) == 0:
        return f"The list is empty"

    list2 = []

    for item in lst1:
        if isinstance(item, str):
            list2.append(item)
    print(f"New List with string: {list2}")

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
creator_string_list(lst1)

print("#" * 100)


# task 9

""""  # Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися,
# якщо користувач ввів слово без букви "h".
"""
def search_h_letter():

    while True:
        input_string = input("Enter any word with letter 'h' , please: ").lower()
        if 'h' in input_string:
            print("Thanks, letter 'h' is present in this word!")
            break
        else:
            print("The word does not contain the letter 'h'. Try again.")

search_h_letter()

print("#" * 100)


# task 10

"""""  #Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()
"""

def find_unique_value():

    input_string = input("Enter the sentence: ")

    unique_value = set(input_string) # set - for getting unique values

    unique_count = len(unique_value) # count unique values

    if unique_count > 10:
        print(True)
    else:
        print(False)

find_unique_value()

