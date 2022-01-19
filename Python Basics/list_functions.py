#List Functions - extend,append,insert,remove,clear,pop,list.index,
#extend
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.extend(lucky_numbers)

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
friends.remove("Jim")
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

