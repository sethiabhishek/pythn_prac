import pickle
import pdb

pdb.set_trace()
dict1 = {"`one":1,"two":2,"three":3}
file1 = open("pickledump",'wb')
pickle.dump(dict1,file1)

dict1 = ''
file1.close()
file1 = open("pickledump","rb")
dict1 = pickle.load(file1)

print dict1
