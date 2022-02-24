'''Static Method:
Static methods are methods that are related to a class but do not need to access any class-specific data.
There is no need to instantiate an instance because we can simply call this method. Static methods are great for utility functions.
They are totally self-contained and only work with data passed in as arguments.
This method is defined inside a class using @staticmethod decorator.'''


'''Class Method:
Class methods are methods that are related to a class and have access to all class-specific data. It uses @classmethod, a built-in function
decorator that gets evaluated after the function is defined.
It returns a class method function. It receives the cls parameter instead of self as the implicit first argument.'''

#Example:
from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18

person1 = Person('Vishnu',28)
person2 = Person.details('Mani',1992)

print(person1.name,person1.age)
print(person2.name,person2.age)
print(Person.check_age(16))


'''Difference:
1.Static methods do not know about the class state. These methods are used to do some utility tasks by taking some parameters where as
the class method takes the class as a parameter to know about the state of that class.

2.Static method cannot access or modify the class state where as class method can access or modify the class state.

3.Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
The class method takes the class as parameter to know about the state of that class.

4.The static method does not take any specific parameter where as the class method takes cls (class) as first argument.
