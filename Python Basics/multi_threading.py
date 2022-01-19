###Multi-Threading
##Definition

'''In any software programming, a thread is the smallest unit of execution with the independent set of instructions.
Multithreading is defined as the ability of a processor to execute multiple threads concurrently. 

The multithreading library is lightweight, shares memory, responsible for responsive UI and is used well for I/O bound applications.

Multiple threads live in the same process in the same space, each thread will do a specific task, have its own code, own stack memory, 
instruction pointer, and share heap memory. 
If a thread has a memory leak it can damage the other threads and parent process.


Why:
Ideally, multithreading can significantly improve the performance of any program.
Python threading allows you to have different parts of your program run concurrently and can simplify your design.
Multiple threads within a process share the same data space with the main thread and can therefore share information 
or communicate with each other more easily than if they were separate processes.'''

##Example

from time import sleep
from threading import * 

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)


class Hi(Thread):
     def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)
    
    
t1 = Hello()
sleep(0.2)
t2 = Hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye")
