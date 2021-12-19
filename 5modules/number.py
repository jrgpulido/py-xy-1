def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False

def isEven(n):
    return not isOdd(n)

def isPositive(n):
    if n > 0:
        return True
    else:
        return False

def isNegative(n):
    return not isPositive(n)
