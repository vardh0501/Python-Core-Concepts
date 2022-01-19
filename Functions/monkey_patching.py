###Monkey Patching

##Definition:
'''Monkey Patching is a technique that allows you to alter the behavior of objects at runtime and has the capability of changing the behaviour.
Moreover, it works without changing user code.


If you work in a big project, most likely you will meet situations, when you would like to change/improve used third-party library behaviour, 
and you try to modify it from your project.'''



##Example 1
class Test:
    def class_method(self):
        print("This is class method")

def monkey_function():
    print("This is monkey function")
    
Test.class_method = monkey_function
Test.class_method()



        
        
