#Colection data type unordered and mutable but does not allow duplicates

#You can use the set function, and it will create a set even if the passed datatype is a list or a tuple...
myset = {1, 2, 3}
print(myset)

#If you wanted to have an empty set you would have to use the set function, otherwise it will be recognised as a dictionary
myset.add(4)
print(myset)
#To add any value inside a set you can just use the add method
#To remove any value inside a set you can just use the remove method
myset.remove(2)
print(myset)
#The discard method will do the same as the remove method, but it will not return an error if it doesn't find the requested element
myset.discard(3)
print(myset)
#The clear method will empty your set, and the pop method will return a random element from the set and also remove it
for i in myset:
    print(i)

#Union and intersection
#To use the union you can use the union method
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

#Calculate the difference of two sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9,}
setB = {1, 2, 3, 10, 11, 12}

#It will return all the elements of the first set that are not in the second set
diff = setA.difference(setB)
print(diff)

# The symmetric_difference method will return a set with all the elements of setA and B that aren't in both of them at the same time
diff1 = setA.symmetric_difference(setB)
print(diff1)

#The update method will include the unshared elements of a set into another
setA.update(setB)
print(setA)

#The intersection_update method will update a set to be its intersected elements with another set
setA.intersection_update(setB)
print(setA)

# We can return a boolean to see if whether the elements of our first set are within the second set
print(setA.issubset(setB))
# We can return a boolean to see if whether the elements of the second set are contained in the first set
print(setA.issuperset(setB))
# We can return a boolean to see if whether our second set contains elements of the first set. If it does contain same elements it will return False
print(setA.isdisjoint(setB))

#If you want to make a copy of a set you will have to use the copy method

#A frozen set is an inmutable version of a set, using the 'frozenset' function