#
# 2do
#

import pickle

t='aTuple',True,3.1

with open('tuple.bin','wb') as fh:
        pickle.dump(t,fh)

print('done...')
