#vaiable scope = where a variable is visible and eligible

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()

#func1 () cant see inside func2() if func2() is outside of func1()

from math import e

def e_func():
    print(e)
e_func()
