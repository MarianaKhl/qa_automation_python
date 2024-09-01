# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися,
# якщо користувач ввів слово без букви "h".

while True:
    input_string = input("Enter the any word with letter 'h' , please: ").lower()
    if 'h' in input_string:
        print("Thanks")
        break
    else:
        print("The word does not contain the letter 'h'. Try again.")
