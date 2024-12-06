adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

print(new_adwentures_of_tom_sawer)
print()

# task 02 ==
""" Замініть .... на пробіл
"""

new_one_adwentures_of_tom_sawer = new_adwentures_of_tom_sawer.replace("....", " ")

print(new_one_adwentures_of_tom_sawer)
print()

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

new_two_adwentures_of_tom_sawer = new_one_adwentures_of_tom_sawer.replace("  ","")

print(new_two_adwentures_of_tom_sawer)
print()

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f"The letter 'h' occurs {new_two_adwentures_of_tom_sawer.count("h")} times.")
print()


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capital_letter = 0

words = new_two_adwentures_of_tom_sawer.split()

for word in words:
    if word.istitle():
        capital_letter += 1

print(f"The {capital_letter} words begin with capital letter.")
print()

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = new_two_adwentures_of_tom_sawer.find("Tom")

print(f"Position, when the word 'Tom' occurs a second time = {new_two_adwentures_of_tom_sawer.find("Tom", first_index +1)}")
print()

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = new_two_adwentures_of_tom_sawer.split(". ")

print(adwentures_of_tom_sawer_sentences)
print()

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence = adwentures_of_tom_sawer_sentences[3]

print(f"fourth_sentence = {fourth_sentence.lower()}")
print()

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentance in adwentures_of_tom_sawer_sentences:
    if sentance.startswith("By the time"):
        print(f"We check that the sentence starts with 'By the time.': {sentance}")
        print()
        break
else:
    print(f"We did not find the sentence that starts with 'By the time.'")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
end_sentance = adwentures_of_tom_sawer_sentences[-1]
word_end_sentance = end_sentance.split()
words_count = len(word_end_sentance)

print(f"The number of words in the last sentence = {words_count}")












