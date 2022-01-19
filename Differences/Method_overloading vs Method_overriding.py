def product(a,b):
    p = a * b
    print(p)

def product(a,b,c):
    p = a * b * c
    print(p)

#product(4,5)
product(4,5,6)


class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')

class DummyRobot(Robot):
    def start(self):
        print('Started.')

r = HelloRobot()
d = DummyRobot()

r.action()
d.action()
