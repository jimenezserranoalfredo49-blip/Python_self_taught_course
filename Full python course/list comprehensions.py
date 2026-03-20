# List comprehension is a compacter and easier way to create lists in Python

doubles = [x * 2 for x in range(1,11)]

triples = [x * 3 for x in range(1,11)]

squares = [x * x for x in range(1,11)]

fruits = ["apple", "orange", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<=0]
print(negative_nums)