# default arguments = a default value for certain parameters
#               used when that argument is omitted
#               make your functions more flexible, reduces # of arguments
#               1.positional, 2.default, 3. Keyword, 4. arbitrary
def net_price(list_price, discount= float(0), tax= float(0.05)):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, discount = 0.1 ))

