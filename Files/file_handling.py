#Reading from external files in python
'''employee_file = open("employees.txt","r")
print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines())
print(employee_file.readlines()[1])
employee_file.close()'''

 
'''employee_file = open("employees.txt","r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()'''


#Appending to files in python

'''employee_file = open("employees.txt","w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()'''


#Writing a new file in python
'''employee_file = open("employees1.txt","w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()'''


#Creating a html file
web_file = open("index.html","w")
web_file.write("<p>This is HTML,</p>")
web_file.close()


