# iterables = object or collection that can return its elements one at a time
#              those elements can be iterated over in a loop

numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(numbers)

name = "Alfredo"

for character in name:
    print(character, end=" ")

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(key, value)