# dog.py
class Dog:
    # properties/attributes
    # Traits/characteristics
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!

    # methods (can do)
    def bark(self):
        print(f"Woof! My Name is {self.name}")

# instantiation call that creates a Dog object:
my_dog = Dog("Rex", "SuperDog")

print(my_dog)
print(my_dog.name)
print(my_dog.breed)

my_dog.bark()

# class => factory
    # Cars
        # color
        # model
        # current_speed
        # accelerate
        # Honk
        # pop the trunk
# class => blueprint/template
# class => cookie cutter
