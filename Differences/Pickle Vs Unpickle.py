import pickle
dogs_dict = {'Ozzy':3,'Filow':8,'Luna':5,'Skippy':10,'Barco':12,'Balou':9,'Laika':16}
filename = 'dogs'
outfile = open(filename,'wb')
pickle.dump(dogs_dict,outfile)
outfile.close()


infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))
