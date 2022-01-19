##Variable Scope:

'''LEGB Rule - Local, Enclosed, Global, Built-in

Local(Funtion):It is the code block or body of any Python function or lambda expression. This Python scope contains the names
that you define inside the function. These names will only be visible from the code of the function. It’s created at function call,
not at function definition, so you’ll have as many different local scopes as function calls. This is true even if you call the same function multiple times,
or recursively. Each call will result in a new local scope being created.

Enclosing (or nonlocal) scope: It is a special scope that only exists for nested functions. If the local scope is an inner or nested function,
then the enclosing scope is the scope of the outer or enclosing function. This scope contains the names that you define in the enclosing function.
The names in the enclosing scope are visible from the code of the inner and enclosing functions.

Global (or module) scope:It is the top-most scope in a Python program, script, or module. This Python scope contains all of the names
that you define at the top level of a program or a module.
Names in this Python scope are visible from everywhere in your code.

Built-in scope: iT is a special Python scope that’s created or loaded whenever you run a script or open an interactive session.
This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python.
Names in this Python scope are also available from everywhere in your code.
It’s automatically loaded by Python when you run a program or script.'''



##Example 1
'''x ='global x'

def test():
    y= 'local y'
    print(y)
   
test()'''

##Example 2
'''x ='global x'

def test():
    y= 'local y'
    print(x)
   
test()'''



##Example 3
'''x ='global x'

def test():
    y= 'local y'
    #print(y)
    print(x)

test()

print(y)'''

##Example 4
'''x ='global x'

def test():
    y= 'local y'
    print(x)

test()

print(x)'''


##Example 5
'''x ='global x'

def test():
    x= 'local x'
    print(x)

test()

print(x)'''

##Example 6
'''#x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)'''

##Example 7
'''def test(z):
    x = 'local x'
    print(z)

test('local z')
#print(z)'''

##Example 8(Built-in)
'''import builtins
print(dir(builtins))
m = min([5,1,4,2,3])
print(m)'''

##Example 9(Enclosing)
'''def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()'''


##Example 10
'''def outer():
    x = 'outer x'
    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)
outer()'''

##Example 11
'''def outer():
    #x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()'''

##Example 12
'''def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()'''


##Example 14
x = 'global x'

def outer():
    #x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)
