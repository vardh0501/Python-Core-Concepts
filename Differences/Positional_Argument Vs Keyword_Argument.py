'''Positional arguments:
Positional arguments are arguments that can be called by their position in the function definition.
Based on the decision making, we have to pass the value into the function.Positional arguments can also be passed to functions using an iterable object.
function(*iterable).'''

#Example:
def positional(a,b):
    first = "a is {}".format(a)
    second = "b is {}".format(b)
    return first,second

print(positional(10,4))


'''Keyword arguments:
Keyword arguments are arguments that can be called by their name.
A keyword argument is an argument passed to a function or method which is preceded by a keyword and an equals sign.function(keyword=value)'''

#Example:
def key(a,b):
    first = "a is {}".format(a)
    second = "b is {}".format(b)
    return first,second

print(key(a=4,b=10))

#Positional argument follows keyword argument but not vice versa
