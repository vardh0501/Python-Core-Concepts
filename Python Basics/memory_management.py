###Memory Management

##Definition
'''Memory allocation can be defined as allocating a block of sequence in the computer to a program.
In python, memory allocation and deallocation method is automatic as we create a garbage collector for python so that the
user doesn't have to do manual garbage collection.

Garbage Collection:
Garbage collection is a process in which the interpreter frees up the memory when not in
use to make it available for other objects.

Reference Counting:
Reference counting works by counting the number of times an object is referenced by other objects in the system.
When references to an object are removed, the reference count for an object is decremented.
When the reference count becomes zero, the object is deallocated.

The GIL is a solution to the common problem of dealing with shared resources, like memory in a computer.
When two threads try to modify the same resource at the same time, they can step on each other’s toes. 
The end result can be a garbled mess where neither of the threads ends up with what they wanted.

Why:
The essential requirement of memory management is to provide ways to dynamically allocate portions
of memory to programs at their request,and free it for reuse when no longer needed.'''

##Example 

x = 10
print(type(x))


y = x
if(id(x) == id(y)):
    print("X and Y refer to the same object")
    
x = x + 1
if(id(x)!= id(y)):
    print("X and Y refer to the different objects")

z = 10
if(id(y)==id(z)):
    print("Y and Z refer to the same memory")
else:
        print("Y and Z refer to the different objects")
    
    
