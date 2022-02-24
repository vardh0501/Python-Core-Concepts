'''Generators:
Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, one at a time, in a special way.
Whenever it needs to generate a value, it does so with the yield keyword rather than return.'''

#Example:
def even_number(x):
    while(x!=0):
        if(x%2==0):
            yield x
        x-=1

for i in even_number(8):
    print(i)


'''Iterator:
The Python Iterator is a object that return one element at a time, and the next() is used for getting the next value.'''

#Example:
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


'''Differences:

1.Python generator usually implemented using function and iterator is implemented using class,
generators use keyword yield and iterator uses keyword return.

2.All the local variables are stored before the yield statement in the generator where as there is no local variable in the iterator.
In a python generator, we can write fast and neat code.

3.To create a generator in python we use the function but to create an iterator function we have to use iterator() and next function().'''
