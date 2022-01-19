###Exeption Handling
##Definition

'''An exception is an error that happens during execution of a program. When that
error occurs, Python generate an exception that can be handled, which avoids your
program to crash.

Why:
Exceptions are convenient in many ways for handling errors and special conditions
in a program. When you think that you have a code which can produce an error then
you can use exception handling.

The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.'''


#Catching Errors in python

number = int(input("Enter a number:"))
print(number)

#try except block

try:
    number = int(input("Enter a number:"))
    print(number)

except:
    print("Invalid Input")


try:
    answer = 10/0
    number = int(input("Enter a number:"))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")


#try except finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
