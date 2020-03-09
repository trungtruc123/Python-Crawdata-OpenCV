import pickle
#example_dict ={1:'2',2:"3",3:"qw"}
#pickle_out = open("dict.pickle","wb")#wb is write byte
#pickle.dump(example_dict,pickle_out)
#pickle_out.close()
pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict)
print(example_dict[3])
