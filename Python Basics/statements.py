##if statements:
'''They a special structure in python where we can make python programs to make decisions. It allows our programs to respond to the input depends
on the data that we are using.if statement is how you perform this sort of decision-making. It allows for conditional execution of a statement or group of statements
based on the value of an expression.'''

is_male = True
if is_male:
    print("You are  male")
else:
    print("You are not male")

is_male = False
if is_male:
    print("You are  male")
else:
    print("You are not male")


is_male = True
is_tall = True
if is_male or is_tall:
    print("You are  male or tall or both")
else:
    print("You are neither male nor tall")


is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a short male")
else:
    print("You are not a male and not tall")


##if statements and comparison operators using function


def max_num(num1,num2,num3):
    if num1 >=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(1,2,3))
        
