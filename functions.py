def funtion_name(name ="default"):
    message = name + " welcome to python!"
    return message

def sumOfAllNumbers(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def square(num):
    return num ** 2

def cube(num):
    return num ** 3