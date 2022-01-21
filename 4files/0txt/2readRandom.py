l=[]

with open('3numeros.txt') as fh:
       for line in fh:
           n=line.strip()
           n=float(n)
           l.append(n)

#
print(l)
print('done...')
