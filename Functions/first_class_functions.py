###First Class Functions

##Defintion
'''First-Class Functions are functions which are treated as so called "First-Class Citizens" (FCC).
A first-class function is not a particular kind of function. All functions in Python are first-class functions.
To say that functions are first-class in a certain programming language means that they can be passed around
and manipulated similarly to how you would pass around and manipulate other kinds of objects (like integers or strings).
You can assign a function to a variable, pass it as an argument to another function, etc.'''

##First Class Citizen
'''First Class Citizens in a programming language are objects which can be used as parameters and return values.It can be passed as an arguemnt
and can be assigned to variables and can be stored in data structures such as hash tables, lists.'''

##Example 1

'''def square(x):
    return x * x

f = square(5)
print(square)
print(f)'''

##Example 2

'''def square(x):
    return x * x

f = square
print(square)
print(f)'''

##Example 3

'''def square(x):
    return x * x

f = square
print(square)
print(f(5))'''



##Example 4

'''def square(x):
    return x * x

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square,[1,2,3,4,5])
print(squares)'''

##Example 5
'''def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube,[1,2,3,4,5])
print(squares)'''

##Example 6

'''def logger(msg):

    def log_message():
        print("Log:",msg)
    return log_message

log_hi = logger("Hi!")
log_hi()'''

##Example 7
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1("Test Headline!")
print_h1("Another Headline!")

print_p = html_tag("p")
print_p("Test Paragraph!")


