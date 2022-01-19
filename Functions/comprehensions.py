###List Comprehension

##Definition

'''List comprehensions is a pythonic way of expressing a ‘for-loop’ that appends to a list in a single line of code.
It provides a concise way to create lists from other iterables

The first expression generates the element in the list where as the second expression generates "for" loop and the third expression 
evaluates the expression for every item in collection.

List comprehensions can also be used for mapping and filtering.

Why:
List comprehensions are also more declarative than loops, which means they’re easier to read and understand.
They can limit the number of lines used in your program.

Disadvantages:
They might make your code run more slowly or use more memory.'''


##Exmple
nums = [1,2,3,4,5,6,7,8,9,10]

#Print the given list 
my_list = [ n for n in nums]
print(my_list)

#Finding the square of numbers in the given list
my_list = [n*n for n in nums]
print(my_list)

#Finding the even numbers from the given list
my_list = [n for n in nums if n%2==0]
print(my_list)


#Print a (letter,num) pair for each letter in 'abcd' and each number in '0123'

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)


my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)



###set comprehension
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = {n for n in nums}
print(my_set)


