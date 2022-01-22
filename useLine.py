#
######### useClass
#
import Line as l
import Point as p

p1 = p.Point(5,3)
p3 = p.Point(4,6)

l1 = l.Line(p.Point(6,4),p.Point(3,3))
l3 = l.Line(p3,p1)

print(type(l1))
t=l1.getLine()
print(type(t))
print(t[0],t[1])
print(t[0].x)
print(t[0].y)

print(l1.isOrthogonal(l3))
print(l3.isOrthogonal(l1))
#print(l3.isOrthogonal(3.1))

print('done...')
