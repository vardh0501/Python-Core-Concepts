#Local Variable:
'''Local variables are those which are initialized inside a function and belongs only to that particular function.
It cannot be accessed anywhere outside the function'''

#Example:
def local_var():
    l = "This is an example syntax for local variable"
    print(l)
local_var()

#Global Variables
'''The global variables are those which are defined outside any function and which are accessible
throughout the program i.e. inside and outside of every function.'''

#Example:
def global_var():
    print("Inside Function",g)

g = "Global Variable"
global_var()
print("Outside Function",g)


'''Using Global Keyword
def new_function():
    new_var+= "Local Variable and"
    print("Inside Function",new_var)

new_var = "Global Variable"
new_function()'''

#To make the above code work, we need to use "global keyword"
def new_function():
    global new_var
    new_var+= "Local Variable"
    print(new_var)
    new_var = "Key Word Added"
    print(new_var)

new_var = "Global Variable"
new_function()
print(new_var)


'''Differences:
1.Local Variables are declared inside a function whereas Global Variables are declared outside the function.
2.If local variables are not initialized, a garbage value is stored where as if global variables are not initialized,then zero is stored as default.
3.Local Variables are created when the function start execution and lost when the function terminate.Global Variables are created before the program's
global execution starts and lost when the program terminates.
4.Data sharing is not possible as data of the local variable can be accessed by only one function where as in global variable,data sharing is possible as
multiple functions can access the same global variable.
5.In local variables, when the value of the local variable is modified in one function,the changes are not visible in another variable where as when the value of
the global variable is modified in one function,changes are visible in rest of the program.


