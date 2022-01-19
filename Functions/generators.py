###Generators

##Definition

'''Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, one at a time, in a special way.
Whenever it needs to generate a value, it does so with the yield keyword rather than return.
Generators don't hold the entire result in the memory.It yields one result at a time.

Why:
Generators are good for calculating large sets of results (in particular calculations involving loops themselves) 
where you don't know if you are going to need all results, 
or where you don't want to allocate the memory for all results at the same time.

Advantages:
Another use for generators (that is really the same) is to replace callbacks with iteration.
Better performance.'''

##Example using return

'''def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)'''


##Generator example
'''def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))'''

##Generator Example using second for loop
'''def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
    print(num)'''



