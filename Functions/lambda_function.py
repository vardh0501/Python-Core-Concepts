###Lambda Function

##Definition

'''It is a small anonymous function.It takes any number of arguments but can have only one expression.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
Basically, its a function within function,and that function is defined without name.

Hence, anonymous functions are also called lambda functions.


Why:
Lambda functions are used when you need a function for a short period of time. 
This is commonly used when you want to pass a function as an argument to higher-order functions, that is,
functions that take other functions as their arguments.
We can also put a lambda definition anywhere a function is expected, and
we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.'''


###Lambda Expression with one input
g = lambda x: 3*x+1
print(g(2))

###Lambda Expression with more than one input
##Combine first name and last name into a single name

full_name = lambda fn,ln:fn.strip().title() + " " + ln.strip().title()
print(full_name("    Vishnu", "SRINI"))


## Finding the max between two numbers
mx = lambda x,y: x if x>y else y
print(mx(8,5))

###Map Function
##Definition
'''The map() function in Python takes in a function and a list as an argument.
The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items
returned by that function for each item.'''


##Example
n = [4,3,2,1]
print(list(map(lambda x:x**2,n)))

###filter
##Definition
'''The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.'''

##Example
n = [4,3,2,1]
print(list(filter(lambda x:x>2,n)))

###reduce
##Definition
'''The reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function 
and an iterable and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the  functools module. '''


##Example
n = [4,3,2,1]
print(reduce(lambda x,y:x*y,n))
