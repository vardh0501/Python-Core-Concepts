###Method Resolution Order

##Definition
'''Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role 
in the context of multiple inheritance as single method may be found in multiple super classes.'''


##Example

class A:
    def display(self):
        print("Class A Method")

class B:
    def display(self):
        print("Class B Method")

class Demo(B,A):
    def show(self):
        print("Class Demo Method")

d = Demo()
d.display()

print(Demo.mro())
