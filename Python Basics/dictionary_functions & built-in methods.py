#In-Built Functions - len(),any(),all(),sorted()

#len()
my_dict = {1:1,2:2,3:3,4:4}
print(len(my_dict))

#any()
print(any({True:False,'':''}))

#all()
print(all({1:1,2:2,"":3}))

#sorted()
new_dict = {3:3,1:1,4:4}
print(sorted(new_dict))


#In-Built Methods - keys(),values(),items(),get(),clear(),copy(),pop(),
#popitem(),fromkeys(),update()

#keys()
print(my_dict.keys())

#values()
print(my_dict.values())

#items()
print(my_dict.items())

#get()
my_marks = {'Physics':67, 'Maths':87}
print(my_marks.get('Physics'))

#clear()
print(new_dict.clear())
print(new_dict)

#copy()

my_new_dict = my_dict.copy()
print(my_new_dict)

#pop()
print(my_new_dict.pop(4))
print(my_new_dict)

#popitem()
my_new_dict = {3:3,1:1,4:4,7:7,9:9}
print(my_new_dict.popitem())

#fromkeys()
print(my_new_dict.fromkeys({1,2,3,4,7},0))

#update()
dict1 = {1:1,2:2}
dict2 = {2:2,3:3}
dict1.update(dict2)
print(dict1)
