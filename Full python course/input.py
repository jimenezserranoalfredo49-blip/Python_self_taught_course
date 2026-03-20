#input() = function hat allows the user to enter some kind of data, and the data will be treated as a string
name = input("What´s your name?:")
age = input("How old are you?:")

print(f"Hello {name}!")
print(f"You are {age} years old")

#Basic exercise, calculate the area of a rectangle

length = float(input("Enter the length (assumed in meters): "))
width = float(input("Enter the width ( assumed in meters): "))
area = length * width

print(f"The area  is {area} m^2")