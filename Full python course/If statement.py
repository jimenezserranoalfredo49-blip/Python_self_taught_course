# if = do something if it is true, therefore it takes booleans
# Else will do something for the case it is not true
#The else statement is the last step, but you can use elif to add more conditions

age = int(input("Enter your age: "))

if age >=18:
    print("You are now signed up!")
elif age<0:
    print("You are not even born yet")
else:
    print("You must be 18+ to sign up")