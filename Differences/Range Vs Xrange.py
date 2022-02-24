'''Differences:
range() – This returns a range object (a type of iterable). Return type - list
xrange() – This function returns the generator object that can be used to display numbers only by looping. Return type - xrange
Only particular range is displayed on demand and hence called “lazy evaluation“.

As range() created a list of all the elements and save it before iterating. Whereas, xrange does not save any element and evaluate each element during each iteration.
So, range() takes more memory to save these elements in the list.

Running xrange() is slower as compared to the range() as xrange evaluates the value of element during each iteration.'''
