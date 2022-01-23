#
#
#

import pickle

with open('list.bin','rb') as fh:
        aList = pickle.load(fh) 

print(type(aList))
print(aList)

print('done...')
