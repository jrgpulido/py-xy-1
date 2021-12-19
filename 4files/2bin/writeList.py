#
# binary files
#

import pickle

aList = ["a list", "including another list", ["inner", "list"]]

with open('list.bin','wb') as fh:
        pickle.dump(aList,fh)

print('done...')
