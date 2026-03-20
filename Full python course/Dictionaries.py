# dictionary = a collection of pairs of {key:value}
#           ordered and changeable

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#get() method will display the value associated to the requested key
#update() method will allow you to add a key and a value to the dictionary or modify an already existing one
#pop() method will delete de the requested key and its associated value
#keys() method will display the keys within your dictionary
#Values() method will display the values within your dictionary
for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")
