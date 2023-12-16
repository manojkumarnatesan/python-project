numbers = [4, 7, 8, 9, 4]


def sum_of_numbers(a, b, c, d, e):
    return a + b + c + d + e


# print(sum_of_numbers(*numbers)) # unpacking lists or tuple

user = {"firstName": "Sathish", "lastName": "Sampath"}


def info(firstName, lastName):
    return f"{firstName} {lastName}"


# print(info(**user))


def lot_of_nummbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(lot_of_nummbers(23, 23, 23, 45, 56, 78))


def packing_person_info(**kwargs):
    print(kwargs)


# packing_person_info(name="Sathish",age=25,city="virudhachalam")

# spreading in python

lst_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_two = [10, 11, 12, 13]

final_lst = [*lst_one,*lst_two]

print(final_lst)
