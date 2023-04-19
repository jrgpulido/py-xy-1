#
######### Class
#
import math as m
import Point as p



#
######### useClass
#
p1 = p.Point(1.0,-1.0)
p3 = p.Point()

print(type(p1))
print(type(p1.x))
print(p1.y)

#set Y
p1.y=4
print(p1.y)
print(type(p1.getPoint()))
print(p1.getPoint())

print(p3.distance(p1))
print(p1.distance(p3))
print(p1.distance(p3.x))
print(p1.angle())


print('done...')
