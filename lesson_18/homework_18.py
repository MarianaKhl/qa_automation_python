def even_numbers_generator(N):
    for i in range(0, N+1, 2):
        yield i

# Example of use
gen = even_numbers_generator(10)
for num in gen:
    print(num)

print('*' * 100)


def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

# Example of use
gen = fibonacci_generator(10)
for num in gen:
    print(num)
print('*' * 100)


class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

# Example of use
lst = [1, 2, 3, 4, 5]
rev_iter = ReverseIterator(lst)
for item in rev_iter:
    print(item)
print('*' * 100)


class EvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        if self.current % 2 == 0:
            result = self.current
        else:
            result = self.current + 1
        self.current = result + 2
        return result

# Example of use
even_iter = EvenNumbersIterator(10)
for num in even_iter:
    print(num)
print('*' * 100)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function call {func.__name__} with args: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"The result of the function {func.__name__}: {result}")
        return result
    return wrapper


# Example of use
@log_decorator
def add(a, b):
    return a + b

add(3, 4)
print('*' * 100)


def exception_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in function {func.__name__}: {e}")
    return wrapper


# Example of use
@exception_handling_decorator
def divide(a, b):
    return a / b

divide(4, 2)  # Successfully
divide(4, 0)  # Exception
print('*' * 100)
