#
######### Class
#

import Point as p

class Line:
    def __init__(self, p1=p.Point(), p3=p.Point()):#constructor
        self.p1 = p1
        self.p3 = p3

    def getLine(self):
        return self.p1, self.p3

    def slope(self):
        n1 = (self.p1.y - self.p3.y)
        d1 = (self.p1.x - self.p3.x)
        return n1/d1

    #def dot(self):#validate

    def isOrthogonal(self,l2):#
        s1=self.slope()
        s2=l2.slope()
        if s1*s2==-1:
            return True
        else:
            return False
