###Variables:

##Definition
'''Variables are just a container that stores certain data values.To create a variable,
you just assign it a value and then start using it.Assignment is done with a single equals sign (=).'''

##Example
character_name = "John"
character_age = "35"


print("There once was a man named " +character_name +  ", ")
print("he was " +character_age+ " years old.")

character_name = "Tom"
character_age = "50"

print("He really liked the name " + character_name +  ", ")
print("but didn't like being " +character_age + ".")



###Data Types:

##Definition

'''Data types are the classification or categorization of data items. It represents the kind of value that tells what operations
can be performed on a particular data.Every value in Python has a datatype. Since everything is an object in Python programming,
Data types are actually classes and variables are instance (object) of these classes.

1.Text Type:	str
2.Numeric Types:	int, float, complex
3.Sequence Types:	list, tuple, range
4.Mapping Type:	dict
5.Set Types:	set, frozenset
6.Boolean Type:	bool
7.Binary Types:	bytes, bytearray, memoryview'''

##Examples

###1.str
##Strings are basically plain text
name = "Roger"
print(type(name))
print(isinstance(name,str))

###2.int
age=1
print(type(age))
print(isinstance(age,int))

###3.float
fraction=0.1
print(type(fraction))
print(isinstance(fraction,float))

###4.complex
complex_num = 1j
print(type(complex_num))
print(isinstance(complex_num,complex))

###5.list
##Lists basically allow you to take a bunch of different values and organize them and store them inside of their own little list structure.
##List is mutable
my_list = ["apple", "banana", "cherry"]
print(type(my_list))
print(isinstance(my_list,list))


###6.tuple
##Tuple is a container where we can store different values.
##Tuple is immutable
my_tuple = ("apple", "banana", "cherry")
print(type(my_tuple))
print(isinstance(my_tuple,tuple))

#Access Tuples

coordinates = (4,5)
print(coordinates[1])

###7.range
my_range = range(10)
print(type(my_range ))
print(isinstance(my_range,range))

###8.dict
my_dict = {
    'id':1,'city':"Chicago",'salary':10000,
    'id':2,'city':"Orlando",'salary':20000,
    'id':3,'city':"Dallas",'salary':30000
}
print(type(my_dict))
print(isinstance(my_dict,dict))

###9.set
my_set = {"apple", "banana", "cherry"}
print(my_set)
print(isinstance(my_set,set)) 


###10.frozenset
my_frozenset = frozenset({"apple", "banana", "cherry"})
print(type(my_frozenset))
print(isinstance(my_frozenset,frozenset))

###11.bool
my_boolean = True
print(type(my_boolean))
print(isinstance(my_boolean,bool))

###12.bytes
my_byte = b"Hello"
print(type(my_byte))
print(isinstance(my_byte,bytes))

###13.bytearray
my_bytearray = bytearray(5)
print(type(my_bytearray))
print(isinstance(my_bytearray,bytearray))

###14.memoryview
my_memoryview = memoryview(bytes(5))
print(type(my_memoryview))
print(isinstance(my_memoryview,memoryview))
