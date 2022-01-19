###Lambda Funtions

##Definition:
'''It is a small anonymous function.It takes any number of arguments but can have only one expression.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
Basically, its a function within function,and that function is defined without name.

Hence, anonymous functions are also called lambda functions.


Why:
Lambda functions are used when you need a function for a short period of time. 
This is commonly used when you want to pass a function as an argument to higher-order functions, that is, functions that take other functions as their arguments.
We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all.
This is the simplicity of lambda functions.'''


##Example 1:
x = lambda a : a + 10
print(x(5))

##Example 2:

#map() with lambda ()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
  
final_list = list(map(lambda x: x*2, li)) 
print(final_list)


#filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
  
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)


#reduce() with lambda()
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
