###Decorators

##Definition
'''A decorator is just a function that takes another function as an argument, adds some kind of functionality,
and then returns another function.So dynamically, it will alter The functionality of your functions
First class functions - pass,return,assign functions to other variables.'''


##Example 1
'''def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function()

outer_function()'''

##Example 2: Outer Function with Assigning a variable
'''def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function()

my_func = outer_function()
my_func()'''

##Example 3: Outer Function With Argument

'''def outer_function(msg):

    def inner_function():
        print(msg)
    return inner_function()

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()'''

##Decorator Function 1


'''def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('Wrapper Executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display Function Ran')

display()'''


##Decorator Function 2


def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('Wrapper Executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display Function Ran')

@decorator_function
def display_info(name,age):
    print('Display_info ran with arguments ({},{})'.format(name,age))
display_info('John',25)

#display()


