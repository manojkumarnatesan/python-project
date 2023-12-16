# normal funtion



def uppercase_decorator(function):
    def wrapper(para1,para2):
        fun = function(para1,para2)
        make_uppercase = fun.upper()
        return make_uppercase
    return wrapper

# gret = uppercase_decorator(greetins)

# print(gret())
@uppercase_decorator
def greetins():
    return "Welcome to python"

# print(greetins())

@uppercase_decorator
def fulName(firstName,lastName):
    return f"{firstName} {lastName}"

# print(fulName("Sathish","Sampath"))

# map(function,iterable)

lst_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def square(x):
    return x ** 2

result = map(square,lst_one)

print(list(result))

# filter(function,iterable)

def evenOrOdd(x):
    if x % 2 == 0:
        return True
    return False

filterResult = filter(evenOrOdd,lst_one)

print(list(filterResult))
from functools import reduce

def addition(x,y):
    return x + y

reduceResult = reduce(addition,lst_one)

print(reduceResult)