# match-case statement alternatives to elif, it will run some code if a value matches a case


#or is represented with "|"
def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" |"Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return False
print(is_weekend("Monday"))