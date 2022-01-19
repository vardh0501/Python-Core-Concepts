#Shallow Copy

import copy
#a = [1,2,3,4,5]
#b = copy.copy(a)
#print(a)
#print(b)

#b[0] = 0
#print(b)
#print(a)


#Deep Copy
a = [1,2,3,4,5]
b = copy.deepcopy(a)
print(a)
print(b)

b[0] = 0
print(b)
print(a)
