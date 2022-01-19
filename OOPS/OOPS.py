##Class and Objects
#class Computer:

#    def __init__(self,cpu,ram):
#        self.cpu = cpu
#        self.ram = ram   

#    def config(self):
#        print("config is",self.cpu,self.ram)

#com1 = Computer("i5",16)
#com2 = Computer("Ryzen 3",0)

#com1.config()
#com2.config()

##Class and Instance Variable

#class Car:

#    wheels = 4

#    def __init__(self):
#        self.mil = 10
#        self.company = "BMW"


#c1 = Car()
#c2 = Car()

#c1.mil = 8
#Car.wheels = 5
#print(c1.company,c1.mil,c1.wheels)
#print(c2.company,c2.mil,c2.wheels)
#print(c1.company,c1.mil,c1.wheels)


##Class,Static & Instance Methods
#Instance Method
#class Student:
#    school = "FIT"

#    def __init__(self,m1,m2,m3):
#        self.m1 = m1
#        self.m2 = m2
#        self.m3 = m3

#    def average(self):
#        return (self.m1 + self.m2 + self.m3)/3

#    def get_m1(self):
#        return self.m1

#    def set_m1(self,value):
#        return self.m1

#s1 = Student(34,67,32)
#s2 = Student(89,32,12)

#print(s2.average())

#Class Method
class Student:
    school = "FIT"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school
        

s1 = Student(34,67,32)
s2 = Student(89,32,12)

print(s2.average())
print(Student.info())


#Static Method
#class Student:
#    school = "FIT"

#    def __init__(self,m1,m2,m3):
#        self.m1 = m1
#        self.m2 = m2
#        self.m3 = m3

#    def average(self):
#        return (self.m1 + self.m2 + self.m3)/3

#    @classmethod
#    def info(cls):
#        return cls.school
#    @staticmethod
#    def info():
#        print("This is student class..in abc module")
        

#s1 = Student(34,67,32)
#s2 = Student(89,32,12)

#print(s2.average())
#Student.info()


##Inner Class


#class Student:

#    def __init__(self,name,rollno):
#        self.name = name
#        self.rollno = rollno
#        self.lap = self.Laptop()

#    def show(self):
#        print(self.name,self.rollno)
#        self.lap.show()

#    class Laptop:

#        def __init__(self):
#            self.brand = "HP"
#            self.cpu = "i5"
#            self.ram = 8

#        def show(self):
#            print(self.brand,self.cpu,self.ram)

#s1 = Student("Navin",2)
#s2 = Student("Jenny",3)


#s1.show()
#lap1 = Student.Laptop()


##Inheritance:
#Single Inheritance
#class A:
#    def feature1(self):
#        print("Feature 1 Working")

#    def feature2(self):
#        print("Feature 2 Working")

#class B:
#    def feature3(self):
#        print("Feature 1 Working")

#    def feature4(self):
#        print("Feature 2 Working")

#Mutilevel Inheritance
#class C(A,B):
#    def feature5(self):
#        print("Feature 5 Working")
        

#a1 = A()
#a1.feature1()
#a1.feature2()

#b1 = B()
#c1 = C()


##Constructor in Inheritance
#class A:

#    def __init__(self):
#        print("in A init")

#    def feature1(self):
#        print("Feature 1 Working")

#    def feature2(self):
#        print("Feature 2 Working")

#class B(A):

#    def __init__(self):
#        super().__init__()
#        print("in B init")

#    def feature3(self):
#        print("Feature 1 Working")

#    def feature4(self):
#        print("Feature 2 Working")

#a1 = B()

#class A:

#    def __init__(self):
#        print("in A init")

#    def feature1(self):
#        print("Feature 1-A Working")

#    def feature2(self):
#        print("Feature 2 Working")

#class B:

#    def __init__(self):
#        print("in B init")

#    def feature1(self):
#        print("Feature 1-B Working")

#    def feature4(self):
#        print("Feature 2 Working")

#class C(A,B):
#    def __init__(self):
#        super().__init__()
#        print("in C init")

#    def feat(self):
#        super().feature2()
        

#a1 = C()
#a1.feat()


##Polymorphism #Mani
#class MyEditor:

#    def execute(self):
#        print("Spell Check")
#        print("Covention Check")
#        print("Compiling")
#        print("Running")

#class Laptop:

#    def code(self,ide):
#        ide.execute()

#ide = MyEditor()
#lap1 = Laptop()
#lap1.code(ide)


#Operator Overloading
#a =5
#b = 6
#print(a+b)
#print(int.__add__(a,b))

#a ="5"
#b = "6"
#print(a+b)
#print(str.__add__(a,b))

#class Student:

#    def __init__(self,m1,m2):
#        self.m1 = m1
#        self.m2 = m2

#    def __add__(self,other):
#        m1 = self.m1 + other.m1
#        m2 = self.m2 + other.m2
#        s3 = Student(m1,m2)
#        return s3

#    def __gt__(self,other):
#        r1 = self.m1 + self.m2
#        r2 = other.m1 + other.m2

#        if r1>r2:
#            return True
#        else:
#            return False
            
#    def __str(self):
#        return "{} {}".format(self.m1,self.m2)

#s1 = Student(58,69)
#s2 = Student(60,65)

#s3 = s1 + s2

#if s1 > s2:
#    print("S1 Wins")
#else:
#    print("S2 Wins")

#print(s1)
#print(s2)


#class Student:

#    def __init__(self,m1,m2):
#        self.m1 = m1
#        self.m2 = m2

#    def sum(self,a=None,b=None,c=None):
#        s = a + b + c
#        return s


#s1 = Student(58,69)
#print(s1.sum(5,9,6))
        
