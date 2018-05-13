import pickle

print("hello world")
filename = 'testing.txt'
outfile = open(filename,'wb')

#stuff to save could be self from an instance for example
stuff_to_save = {'stuff1': 'delicious', 'more_stuff': 'rock on'}
pickle.dump( stuff_to_save ,outfile)
outfile.close()


# this is the code the reopens and gets the python data
infile = open(filename,'rb')
loaded_data = pickle.load(infile)

infile.close()


print('this is our saved python we opened', loaded_data["stuff1"])
print(loaded_data)
