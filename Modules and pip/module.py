###Modules

##Definition

'''Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file. A Python module can have a set of functions, 
classes or variables defined and implemented.

We have buit-in and user defined models.

Some modules are available through the Python Standard Library and are therefore installed with your Python installation. 
Others can be installed with Python’s package manager pip. 
Additionally, we can create our own Python modules since modules are comprised of Python .py files.

We can use any Python source file as a module by executing an statement such as "import module"'''

##Locally installed modules:
help('modules')
pip list

import sys
dir(sys)- list of directory,commands

##pip freeze

'''pip freeze is a very useful command, because it tells you which modules you've installed with pip install and 
the versions of these modules that you are currently have installed on your computer.
In Python, there are lot of things that may be incompatible, such as certain modules being incompatible with other modules.

For example, you may install the latest version of Django but a previous module that you have installed may no longer be compatible with the new version of Django. 
Therefore, you may get errors when you run code.
In instances like this, and many more other instances, using pip freeze to see what modules and versions of 
each you have can be very important and can determine whether a particular application will work or not.
pip freeze is a command that works across practically all operating systems, including Windows, Linux, and Mac.'''


##PEP 8:
'''It is a document that provides guidelines and best practices on how to write Python code.
PEP stands for Python Enhancement Proposal that describes new features proposed for Python and documents aspects of Python, like design and style.
It also has a lot of programming recommendations and useful tips on various topics, which aim to improve readability and reliability of your code.

Why:
PEP 8 exists to improve the readability of Python code.
If you’re new to Python, it can be difficult to remember what a piece of code does a few days, or weeks, after you wrote it. 
If you follow PEP 8, you can be sure that you’ve named your variables well. 
You’ll know that you’ve added enough whitespace so it’s easier to follow logical steps in your code. You’ll also have commented your code well.'''
