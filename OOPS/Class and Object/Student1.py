#Class Function:
#It is a function that we can use inside of a class and with that we can either modify
#the object of the class or give a specific information about the objects.

class Student1:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        

        

