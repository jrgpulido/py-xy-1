#
# stats
# module
#

import math

def sum(lst):
    s=0
#    for k in range(len(lst)):
    for k in lst:
#        s+=lst[k]
        s+=k
    return s

def avg(l):
    return sum(l)/len(l)

def min(l):
    m=l[0]
    for k in l:
        if k<m:
            m=k
    return m

def max(l):
    m=l[0]
    for k in l:
        if k>m:
            m=k
    return m

def range(l):
    mx=max(l)
    mn=min(l)
    return mn,mx

def std(l):
    a=avg(l)
    s=0.0
    for k in l:
        s+=(k-a)*(k-a)
    return math.sqrt(s/len(l))

def mode(l):
    l.sort()#data must be sorted
    c1 = c2 = 0
    m1 = m2 = l[0]
    for k in l:
        if m1 == k:
            c1 += 1
        elif c1 >= c2:
            c2 = c1
            m2 = m1
            m1 = k
            c1 = 1
    if c1 > c2:
        return m1, c1
    else:
        return m2, c2
    
#
# what about multi-mode data
#

def modePrint(l):
    l.sort()#data must be sorted
    c1 = c2 = 0
    m1 = m2 = l[0]
    for k in l:
        if m1 == k:
            c1 += 1
        elif c1 >= c2:
            c2 = c1
            m2 = m1
            m1 = k
            c1 = 1
    if c1 > c2:
        print('howMany', m1, '->', c1)
    else:
        print('howMany', m2, '->', c2)        
