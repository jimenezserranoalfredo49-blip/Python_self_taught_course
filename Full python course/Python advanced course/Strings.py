# Strings are an ordered and immutable data type used for text representation

#You can use double quotes or single quotes to define a string

print("I love python")

#Triple quotes are used for multiline strings or documentation within a code

#To access any character you also use the square braquets, like in lists

my_string = "Hello World"
char = my_string[0]
print(char)

# The strip method removes the white spaces within a string
# The upper method will make all characters upper cases
# The lower method will do the opposite
# The startswith method will return True if it starts with the provided element
# The endswith does the opposite
# The find method will return the index of the requested character, returning -1 if it does not find the character
# The count method will display the amount of times the character is within the string
# The replace method will replace the requested characters by the provided new ones
# Using the split method will separate your string onto a list (it uses spaces as the guide/limiter)
my_string2 = "How are you doing"
my_list = my_string2.split()
print(my_list)

# With the join method you can turn a list onto a string

new_string = " ".join(my_list)
print(new_string)
