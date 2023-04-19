#list comprehension examples

#1
mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print(secs)

#2
lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

#3 greater
y=[x for x in [3,-2,1] if x>2]
print(y)
