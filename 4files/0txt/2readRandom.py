l=[]

with open('3numeros.txt') as fh:
       for line in fh:
           n=line.strip()
           n=float(n)
           l.append(n)

print(max(l))
print(min(l))
print('sum: '+str(sum(l)))
#vs
print('sum: ',sum(l))
print(sum(l)/len(l))
