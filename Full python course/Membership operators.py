#Memberships operators = used to test whether a value or variable is found in a sequence

word = "APPLE"

letter = input("Guess a letter in the secret word: ").capitalize()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was nos found")

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} was found")

grades = {"Sandy": "A",
          "Squidward ": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student_2 = input("Enter the name of a student: ")

if student in grades:
    print(f"{student_2}'s grade is{grades[student_2]}")
else:
    print(f"{student_2} was not found")