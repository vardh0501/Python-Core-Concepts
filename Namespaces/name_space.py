###Name Spaces

##Definition

'''A namespace is a type of structure which is used to organize the symbolic names assigned to objects in a Python program.

It is basically a system to make sure that all the names in a program are unique and can be used without any conflict.
We already knew that everything in Python—like strings, lists, functions, etc.—is an object. 

It is a collection of currently defined symbolic names along with information about the object that each name references.
In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.'''



##Types

'''Local Namespace: This namespace includes local names inside a function. This namespace is created when a function is called, 
and it only lasts until the function returns.

Global Namespace: The global namespace contains any names defined at the level of the main program. Python creates the global namespace when '
the main program body starts, and it remains in existence until the interpreter terminates.

Built-in Namespace: This namespace includes built-in functions and built-in exception when you start the python interpreter.'''


