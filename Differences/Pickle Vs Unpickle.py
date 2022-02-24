'''Pickling:
The pickle module implements binary protocols for serializing and de-serializing a Python object structure. 
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream.'''

#Example
import pickle
dogs_dict = {'Ozzy':3,'Filow':8,'Luna':5,'Skippy':10,'Barco':12,'Balou':9,'Laika':16}
filename = 'dogs'
outfile = open(filename,'wb')
pickle.dump(dogs_dict,outfile)
outfile.close()


'''Unpickling:
“unpickling” is the inverse operation, 
whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.'''


#Example
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))

