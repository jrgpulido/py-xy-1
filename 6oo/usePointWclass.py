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
        if isinstance(p,Point):#validate
            x1 = p.x
            y1 = p.y
            x2 = self.x
            y2 = self.y
            return m.sqrt(((x1-x2)**2)+((y1-y2)**2))
        else:
            print('Point is required')

    def angle(self):#validate2do
        return m.atan(self.y/self.x)#radians


#
######### useClass
#


p1 = Point(1,-1)
p3 = Point()

print(type(p1))
print(type(p1.x))
print(p1.y)
p1.y=4
print(p1.y)
print(type(p1.getPoint()))
print(p1.getPoint())

print(p3.distance(p1))
print(p1.distance(p3))
print(p1.distance(p3.x))
print(p1.angle())


print('done...')
