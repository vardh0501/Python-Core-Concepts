'''Method Overloading:
It is a form of Compile time polymorphism. In the case of method overloading, more than a single method belonging to a
single class can share a similar method name while having different signatures. One can use method overloading for adding more to the behavior of concerned methods.
A user won’t need more than one class for implementing it.

Python does not provide any support for method overloading. A user may overload all the methods, but they will be capable of using only the latest defined method.'''

#Example:
def product(a,b):
    p = a * b
    print(p)

def product(a,b,c):
    p = a * b * c
    print(p)

#product(4,5)
product(4,5,6)

'''Method Overloading:
It is a type of run-time polymorphism. In the case of method overriding, the child class provides a
specific implementation of any method (that the parent class already provides). Method overriding assists a user in changing the behavior of already existing methods. One needs at least two classes to implement it. Inheritance is also a prerequisite in method overriding.
It is because it occurs between both the methods- superclass (parent class) and child class.'''

#Example:

class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')

class DummyRobot(Robot):
    def start(self):
        print('Started.')

r = HelloRobot()
d = DummyRobot()

r.action()
d.action()


'''Differences


1.One may or may not require inheritance in the case of method overloading.
Inheritance is a prerequisite in the case of method overriding.


2.One can perform method overloading between methods that reside within a class.
One can perform method overriding between both the methods- child class and parent class (or superclass).

3.
We use method overloading for adding more to the behavior of all the methods.
We use the method overriding for changing the behaviour of the methods that already exist.

4.
A user won’t need more than one class for implementing method overloading.
A user would always require at least two classes for implementing method overriding. It always works with more than one class.
