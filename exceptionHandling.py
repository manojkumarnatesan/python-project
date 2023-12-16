# print(1)
# print(2)
# print(3)
# try:
#     print(4/0)
# except:
#     print("Exception was occured")
# print(5)
# print(6)
# print(7)

try:
    name = input("Enter Your name: ")
    year_born = input("Enter your born year: ")
    age = 2023 - int(year_born)
    print(f"you are {name}. And your age is {age}")
# except TypeError:
#     print("Type error was occured")
# except ValueError:
#     print("Value error occured")
# except ZeroDivisionError:
#     print("Zero division error")
except Exception as e:
    print(Exception)
else:
    print("Its usally runs with try block ")
finally:
    print("Its always runs")