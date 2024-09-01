#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()

input_string = input("Enter the sentence: ")

unique_values = set(input_string) # set - for getting unique values

unique_count = len(unique_values) # count unique values

if unique_count > 10:
    print(True)
else:
    print(False)
