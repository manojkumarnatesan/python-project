def sum_numbers(nums):
    return sum(nums)


def higherOrderFunction(fun,list):
    summation = fun(list)
    return summation

result = higherOrderFunction(sum_numbers,[1,2,4,85,89])

# print(result)

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def higher_order_function(type):
    if type == 'square':
        return square
    if type == 'cube':
        return cube
    
result_fun = higher_order_function("square")

print(result_fun(8))