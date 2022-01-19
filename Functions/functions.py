#Functions

##It is a collection of python code that performs specific task.
##Allow you to break code.

#Basic Function
def say_hi():
    print("Hello User")
print("Top")
say_hi()
print("Bottom")

#parameter is a piece of information that we we will give it to function.
#Function with single paramter

def say_hi(name,age):
    print("Hello " + name + ",you are " + age)

say_hi("Mike","35")
say_hi("Steve","70")


#Function with more than one paramteres

def say_hi(name,age):
    print("Hello " + name + ",you are " + str(age))

say_hi("Mike",35)
say_hi("Steve",70)

#Return statement
#To get information back from the python function, and function can communicate us that's
#called return statement.

def cube(num):
    return num * num * num
result = cube(4)
print(result)


#Note:After using return keyword, python is going to break out of the function




###zip function
#The first index of the first list matches with the first index with the second list

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
print(my_dict)

my_dict = {name:hero for name,hero in zip (names,heros)}
print(my_dict)

my_dict = {name:hero for name,hero in zip (names,heros) if name!='Peter'}
print(my_dict)




