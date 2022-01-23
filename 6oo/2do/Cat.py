#
######### Class
#

class Cat:
    '''
    This is a description
    
    This adds more help
    
    Arguments
    
    Return
    '''
    
    
    def __init__(self, id=0, name=0, weight=0):#constructor
        self.id = id
        self.weight = weight
        self.name = name



    def getCat(self):
        return (self.id,self.name,self.weight)

import random as r

l=[]
q=50
for k in range(q):    
    id=r.randint(1, q)
    c=Cat(id,'name'+str(id),r.randint(1, 7))
    print(c.getCat())
    

    
    