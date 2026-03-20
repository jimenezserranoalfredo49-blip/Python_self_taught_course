# logical operators = evaluate multiple conditions (or, and, not)
#               or = like in logic, at least one of the statements is true
#               and = like in logic, both conditions must be true
#               not = inverts the given condition

temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor even is cancelled")
else:
    print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp<=0 and is_sunny:
    print("Its cold outside")
    print("It is sunny")