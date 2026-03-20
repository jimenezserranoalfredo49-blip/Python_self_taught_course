#A tuple is quite similar to a list, but it is inmutable
#If the tuple contains only one element it won't be recognised as a tuple, but as a string
#In order to fix that just add a comma at the end
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

#To index is exactly the same as a list because both are ordered

#The following code won't work because a tuple is inmutable
#mytuple[0] = "Tim"

#Iteration is quite the same as the one in a list
for i in mytuple:
    print(i)
if "Max" in mytuple:
    print("Yes")
else:
    print("No")

my_tuple = ('a', 'b', 'c','d', 'e')
#To get the number of elements ou can just use the len function
#To count some element inside the tuple use the count method and put the data you want to count
#To find the index of an element you use the index method and pass the element you want to index
#convert a tuple to a list and viceversa with the list and tuple functions
#To slice in tuple is the same way as in a list, using the :
#You can assign as many variables as elements are in the uple

name, age, city = mytuple
print(name,age,city)

my_tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple2
print(i1)
print(i2)
print(i3)