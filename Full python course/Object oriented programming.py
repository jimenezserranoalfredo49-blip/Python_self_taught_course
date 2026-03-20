# Object = a "bundle" of related attributes (variables) and methods (functions)
# a "class" is needed to create many objects
# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model} of the year {self.year}")

    def stop(self):
        print(f"You stop the {self.color} {self.model} of the year {self.year}")

#classes may take a lot of space so you can put it in another file within the folder you are working on and just import it)


car1 = Car("Mustang", 2024, "red", False)

car2 = Car("Corvette", 2025, "Blue", False)

car3 = Car("Charger", 2026, "Yellow", True)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)