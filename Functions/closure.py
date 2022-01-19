###Clousure

##Definition:
'''A Closure is a function object that remembers values in
enclosing scopes even if they are not present in memory.'''

##Example 1:
'''def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func()
outer_func()'''


##Example 2:

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func()

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func()
hello_func()

