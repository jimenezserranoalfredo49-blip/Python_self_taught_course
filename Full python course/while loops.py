# while loop  will execute a certain code WHILE a condition is true

age = int(input("Enter your age: "))

while age < 0:
    print("Age can not be negative")
    age= int(input("Enter your age: "))

print(f"You are {age} years old")
