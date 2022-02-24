'''1.List vs Tuple
List - Mutable
Tuple - Immutable

Implication of iterations is Time-consuming
Implication of iterations is comparatively Faster

The list is better for performing operations, such as insertion and deletion
Tuple data type is appropriate for accessing the elements

Lists consume more memory
Tuple consume less memory as compared to the list

Lists have several built-in methods
Tuple does not have built-in methods.'''

#Example
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)


'''2.Tuple vs Dict

Tuple won't need any key value pairs like Dictionary.
A tuple can contain only the predefined number of values, in dictionary there is no such limitation.
A tuple can contain different values with different datatype while a dictionary can contain only one datatype value at a time
Tuples are particularly useful for returning multiple values from a function. A dictionary can be used as a model object.'''


#Example:
t_var = (3,4,5)
print(t_var)

age_dict = {"Gabby": 8 , "Maelle": 5}
print(age_dict)

'''3.List Vs Dict

List is a collection of index values pairs.
Dictionary is a hashed structure of key and value pairs.

List is created by placing elements in [ ] seperated by commas “, “
Dictionary is created by placing elements in { } as “key”:”value”, each key value pair is seperated by commas “, ”

The indices of list are integers starting from 0.
The keys of dictionary can be of any data type.

The elements are accessed via indices.
The elements are accessed via key-values.'''

'''4.List Vs Set
List is the datatype offered by Python. The users can write it as the list whose values can be separated by a comma and are written between the square brackets.
It can be converted into different data types, and the users can store any element of data in it. Therefore, the List is mutable.
It is ordered.

Sets are the unordered collection of data types in Python, which are mutable and iterable. Sets do not have any repetition of identical elements.
It is the unordered collection of items or data types in Python.
The order of elements stored in it is not fixed. The order of set elements can be changed.'''

#Example:
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a|b)
print(a & b)

'''5.List Vs Arrays

An array is also a data structure that stores a collection of items. Like lists, arrays are ordered, mutable, enclosed in square brackets,
and able to store non-unique items.

But when it comes to the array's ability to store different data types, the answer is not as straightforward. It depends on the kind of array used.

To use arrays in Python, you need to import either an array module or a NumPy package.'''

#Example
import array as arr
array_new = arr.array("i", [3, 6, 9, 12])
print(array_new)



'''Summary:
If we need to store duplicates, lets go for List or Tuple.
For List vs. Tuple, if we do not intend to mutate, lets go for Tuple.
If we do not need to store duplicates, lets go for Set or Dictionary.'''


