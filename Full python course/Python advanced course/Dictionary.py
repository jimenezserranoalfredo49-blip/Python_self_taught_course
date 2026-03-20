#A dictionary is a mutable and unordered dtype which consists of key:values pairs

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict["name"])
print(mydict["age"])
print(mydict["city"])

#the dict function will also create a dictionary
mydict2 = dict(name="Max", age=28, city="New York")
print(mydict2)

#To add another key-value pair at the end of the dictionary you simply put it like this
mydict["email"] = "max@xyz.com"
print(mydict)
#If the key had already existed it would have updated the value
#If you use the pop method you will remove a key alongside its value
#You can use the popitem method will remove the last key of the dictionary

#The way to use an if statement with a dictionary is quite simple
if "name" in mydict:
    print(mydict["name"])
try:
    print(mydict["lastname"])

except KeyError:
    print("Error")

#Looping through a dictionary
#The key method will return all the keys inside a dictionary in form of a list

for key in mydict.keys():
    print(key)
for key, value in mydict.items():
    print(key, value)

#To copy a dictionary you have to be careful because if you modify the copy you will also modify the original if you had just assigned the copy to be the original
mydict_copy = mydict.copy()
mydict_copy["job"] = "Computer science engineer"
print(mydict_copy)

#To update a dictionary you can use the "update" method
my_dict = {"name": "Max", "age": 28, "city": "New York"}
my_dict2 = dict(name = "Mary", age = 27, email = "mari01@gmail.com")
my_dict.update(my_dict2)
print(my_dict)

#Any inmutable type of data can be used as a key in a dictionary

my_dict3 = {3: 9, 6: 36, 9: 81}
print(my_dict3)

value = my_dict3[3]
print(value)

mytuple = (8, 7)
my_dict4 = {mytuple: 15}
print(my_dict4)

#If you threw a list it wouldn't work because a list is mutable