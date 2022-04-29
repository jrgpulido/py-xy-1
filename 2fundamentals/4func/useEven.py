#
# do NOT forget to reuse
#

def isOdd(x):
    return not isEven(x)
#ends
    
def isEven(x):
    if x%2 == 0:
        return True 
    else:
        return False
#ends 

print(isOdd(7))
print(isOdd(6))

print(isEven(7))
print(isEven(6))
