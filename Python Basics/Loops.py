###Loops
'''Iteration means executing the same block of code over and over, potentially many times.
A programming structure that implements iteration is called a loop.'''

##while loop(Indefinite Iteration)

'''It is basically a structure in python which allows us to loop through and executing block of code multiple times repeatedly until a certain condition was false.
With indefinite iteration, the number of times the loop is executed isn’t specified explicitly in advance. Rather, the designated block is
executed repeatedly as long as some condition is met.'''
 
##Example
i = 1
while i <=10:
    print(i)
    i = i + 1

print("Done with loop\n")


###for loop(Definite iteration)
'''With definite iteration, the number of times the designated block will be executed is specified explicitly at the time the loop starts.
It is a special type of loop which allows to loop over different collection and items. It loops through series of numbers.'''

##Example 1

for letter in "Giraffe Academy":
    print(letter)


    
#Example 2

friends = ["Jim","Karen","Kevin"]
for friend in friends:
    print(friend)

friends = ["Jim","Karen","Kevin"]
for index in range(3,10):
    print(index)


##Exponent Function:
#It allows to take a certain number and raise it to a specific power.
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))


###Nested for loop:
##For loop inside for loop

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)
    print(row)
    
