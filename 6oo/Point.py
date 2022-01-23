#
######### Class
#

import math as m

class Point:
    def __init__(self, x=0, y=0):#constructor
        self.x = x
        self.y = y
        #self.name = 'noName'

    def getPoint(self):
        return self.x, self.y

    def distance(self,p):
        if isinstance(p,Point):
            x1 = p.x
            y1 = p.y
            x2 = self.x
            y2 = self.y
            return m.sqrt(((x1-x2)**2)+((y1-y2)**2))
        else:
            print('Point is required')

    def angle(self):#validate
        return m.atan(self.y/self.x)
