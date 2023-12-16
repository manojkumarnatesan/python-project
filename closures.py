
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add(5)

print(add_ten())