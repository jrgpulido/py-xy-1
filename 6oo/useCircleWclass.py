#
######### Class
#

import Point as p

class Circle:
    def __init__(self, p=p.Point(), r=0):#constructor
        self.p = p
        self.r = r
        
    def inCircle(self, p=p.Point()):#validate
        if p.distance(self.p) < self.r:
            return True
        else:
            return False
        
    def onCircle(self, p=p.Point()):#validate
        if p.distance(self.p) == self.r:
            return True
        else:
            return False

    def outCircle(self, p=p.Point()):#validate
        if p.distance(self.p) > self.r:
            return True
        else:
            return False
    
        

#
# useClass
# stepByStep
#

c=Circle(p.Point(0,0),1)
c1=Circle(1)

p1=p.Point(1.0,1.0)#out
p2=p.Point(0,1)#on
p3=p.Point(0,.3)#in

c.inCircle(p1)
c.inCircle(p2)
c.inCircle(p3)

c.onCircle(p1)
c.onCircle(p2)
c.onCircle(p3)

c.outCircle(p1)
c.outCircle(p2)
c.outCircle(p3)

#
# try
#
print(type(Circle))
isinstance(c,Circle)
print(type(p))
isinstance(p1,p.Point)
print(type(p.Point))
print(p.Point().getPoint())
