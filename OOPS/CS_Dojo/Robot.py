class Robot:

    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        

#Object1
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

#object2
r2 = Robot()
r2.name = "Jerry"
r2.color = "Blue"
r2.weight = 40

#Attributes
r1.introduce_self()
r2.introduce_self()

