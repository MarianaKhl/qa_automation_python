def sum_numbers(s):
    try:
        numbers = map(int, s.split(','))
        return sum(numbers)
    except ValueError:
        return "Characters cannot be converted to numbers!"

string_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
for s in string_array:
    print(sum_numbers(s))

