# arbitrary positional arguments = pass multiple non-key arguments

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3))

#arbitrary keyword arguments =  pass multiple keywords-arguments

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(Street = "123 Fake ST", city = "Detroit", State = "MI", Zip = "54321")