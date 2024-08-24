alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n/
'"That depends a good deal on where you want to get to," said the Cat.\n/
'"I don't much care where ——" said Alice.\n/
'"Then it doesn't matter which way you go," said the Cat.\n/
'"—— so long as I get somewhere," Alice added as an explanation.\n/
'"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"
'"That depends a good deal on where you want to get to," said the Cat.
'"I don't much care where ——" said Alice.
'"Then it doesn't matter which way you go," said the Cat.
'"—— so long as I get somewhere," Alice added as an explanation.
'"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'"""

print("Number of single quotes:", alice_in_wonderland.count("'"))


# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_s = 436402
azov_sea_s = 37800

seas_s = black_sea_s + azov_sea_s
print("Загальна площа Чорного та Азовського морів:" {seas_s} "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum = 375291
storage_1_2 = 250449
storage_2_3 = 222950

storage1 = sum - (storage_2_3)
storage3 = sum - (storage_1_2)
storage2 = sum - (storage1 + storage3)

print(f"storage_1 = {storage1}, storage_2 = {storage2}, storage_3 = {storage3}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
year = 12
payment_months = year + year/2
price_a_month = 1179
laptop_price = payment_months * price_a_month

print(f"Laptop price =  {laptop_price}")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"a = {a}, b =  {b}, c = {c}, d = {d}, e = {e}, f = {f}")



# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big = 274 * 4
pizza_average = 218 * 2
juice = 35 * 4
pie = 350 * 1
water = 21 * 3

sum = pizza_big + pizza_average + juice + pie + water

print(f"All price for the party = {sum}")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos_sum = 232
album_list_include = 8

need_lists = photos_sum / album_list_include
print(f"Need lists in album is about = {need_lists}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

whole_trip = 1600
petrol = (whole_trip/100)*9
gas_tank = 48
stops = petrol / gas_tank

print(f"{petrol} liters of petrol will be needed, and at least {stops} times you need to go to the gas station")

