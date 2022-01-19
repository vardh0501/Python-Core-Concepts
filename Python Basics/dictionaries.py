##Dictionary:
#It is a special structure in python which allows us to store information using
#key value pairs.

#word ->key
#value->definition

month_conversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    
}
print(month_conversions["Nov"])
print(month_conversions.get("Dec"))

#Default value

print(month_conversions.get("Luv","Not a valid key"))

##Default Dict 
'''Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dict class that returns a dictionary-like object. 
The functionality of both dictionaries and defualtdict are almost same except for the fact that defaultdict never raises a KeyError. 
It provides a default value for the key that does not exists.'''

def_value(): 
    return "Not Present"
       
d = defaultdict(def_value) 
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"]) 

Output:
1
2
Not present

##Counter Obj:
'''A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.'''

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
	cnt[word] += 1
cnt
Counter({'blue': 3, 'red': 2, 'green': 1})
