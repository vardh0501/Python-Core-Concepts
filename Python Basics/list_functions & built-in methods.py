#List Functions - len(),max(),min(),sum(),sorted(),list(),any(),all()
#len()
my_list = [3,1,2]
print(len(my_list))

#max()
print(max(my_list))

#min()
print(min(my_list))

#sum()
print(sum(my_list))

#sorted()
print(sorted(my_list))

#list()
print(list("abc"))

#any()

print(any([1,""]))

#all
print(all(['','','1']))


#List Built-in methods - extend,append,insert,remove,clear,pop,list.index,
#extend
prime_numbers = [2,3,5]
lucky_numbers = [4,8,15,16,23,42]
lucky_numbers.extend(prime_numbers)
print(lucky_numbers)

#append
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.append("Creed")
print(friends)

#insert
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.insert(1,"Kelly")
print(friends)

#remove
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.remove("Jim")
print(friends)

#clear
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.clear()
print(friends)

#pop
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.pop()
print(friends)

#count
friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby"]
print(friends.count("Jim"))

#sort
friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby"]
friends.sort()
print(friends)

#reverse
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby"]
lucky_numbers.reverse()
print(lucky_numbers)


#copy
friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby"]
friends_2 = friends.copy()
print(friends_2)



#2D Lists

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print(number_grid[0][1])
print(number_grid[2][1])

