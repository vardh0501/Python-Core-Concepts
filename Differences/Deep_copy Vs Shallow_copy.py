'''Shallow copy Definition

A shallow copy also makes a separate new object object or list, but instead of copying the child elements to the new object, 
it simply copies the references to their memory addresses. 
Hence, if you make a change in the original object, it would reflect in the copied object, and vice versa.'''

#Example:

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)


'''Deep copy Definition

A deep copy makes a new and separate copy of an entire object or list with its own unique memory address. 
What this means is that any changes you make in the new copy of the object/list won't reflect in the original one. 
This process happens by first creating a new list or object, followed by recursively copying the elements from the original one to the new one.'''

#Example:
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

