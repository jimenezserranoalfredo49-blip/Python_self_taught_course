#collection = single "variable" that can store multiple variables
# List = [] ordered and changeable
# Set = {} unordered and immutable
# Tuple = () ordered and unchangeable

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[::2])
#the in operator will return a boolean if the requested character belongs to the called collection

#append() method will add another element to the end of the list
#remove() method will remove the chosen element of a collection
#sort() method will reorder the elements of the collection in alphabetical order
#reverse() method will reorder the elements in the opposite of the initial order
#index() method will display the position of the requested character
#count() method will display the amount of times a certain character appears

names = ["John", "Arthur", "Mark", "Silvia"]
#sets are unordered so the index() function will not work
#add() method will still work tho
#pop() will remove the first element, but have in mind that it will be random
#if you have two times the same character it will only display it once

objects = ["Book", "Pencil", "Backpack"]
# Tuples are the fastest way of collections

things = [fruits, names, objects]

print(things[1][3])
for elements in things:
    print(elements)

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()