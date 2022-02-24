'''Class Variables:
Class variables are defined within the class construction. Because they are owned by the class itself,
class variables are shared by all instances of the class. They therefore will generally have the same value
for every instance unless you are using the class variable to initialize a variable.

Defined outside of all the methods, class variables are, by convention, typically placed right below the class header and
before the constructor method and other methods.'''


#Example:
class Shark:
    animal_type = "fish"

new_shark = Shark()
print(new_shark.animal_type)

'''Instance Variables:
Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.
Unlike class variables, instance variables are defined within methods.'''

#Example:
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)

'''Differences:
1.Class variables are declared inside the class definition but outside any of the instance methods and constructors where as
Instance variables are declared inside the constructor i.e., the __init__() method.

2.Class variables are shared by all instances where as Instance variables are not shared by objects. Every object has its own copy of the instance attribute

3.Class variables are created when the program begins to execute where as instance variables gets created when an instance of the class is created.

4.Changes made in the class variable will reflect in all objects where as in instance variable,changes made to these variables through one object
will not reflect in another object.


