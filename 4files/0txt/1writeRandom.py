#
# txt
#

import random as r

fh = open('3numeros.txt', 'wt')
for k in range(3):
    fh.write(str(r.random())+'\n')    

fh.close()

print('done...')
