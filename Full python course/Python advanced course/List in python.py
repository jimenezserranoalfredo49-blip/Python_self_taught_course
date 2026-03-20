# List is an ordered and mutable kind of dtype which allows duplicate elements

mylist = ["Banana", "Cherry", "Apple"]
print(mylist)
#So, the len() function will check how many elements are inside a list
print(len(mylist))

#The append method will allow you to insert a certain data inside the list
mylist.append("lemon")
print(mylist)

#But if you want to insert it in a certain position you will have to use the insert method
mylist.insert(1, "blueberry")
print(mylist)

#To remove an item you will use the pop method which will remove the last item of the list
item = mylist.pop()
print(item)
print(mylist)

#To remove a certain item you will hae to use the remove method
item_1 = mylist.remove("Apple")
print(mylist)

#To remove all elements you can use the clear method
#The reverse method will also reverse the list
item_2 = mylist.clear()
print(mylist)

#To sort your list you can use the sort method or the sorted() function too
mylist2 = [4, 3, 1, -1 ,2, 10]
mylist2.sort()
print(mylist2)

new_list = sorted(mylist2)
print(new_list)

#To create a new list with the same elements multiple times
mylist3 = [0] * 5
print(mylist3)

mylist4 = [1, 2, 3, 4, 5]
new_list2 = mylist3 + mylist4
print(new_list2)

#Slicing allows you to access a part of your list with a :
#If you put a second : you will modify the step

mylist5 = [1,2,3,4,5 ,6,7,8,9]
a = mylist5[::2]
print(a)

#To copy a list and not modify it you will have to use the copy method because otherwise if you modify the copy you will also modify the original
#Another way of doing it is slicing, this way the original also remains unchanged

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
list_cpy.append("apple")
print(list_cpy)
print(list_org)

#Let's create a new list that consists of the square of an already existing one
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i*i for i in a]
print(a)
print(b)