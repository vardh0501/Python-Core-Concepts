##Modules in python:
#Its a python file that we can import into python files that we are currently
#working on.

#Built in Modules -
#Third party External Modules



import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney","Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)


#pip is used to install python. its a package manager.
