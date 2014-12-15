def factorial(n):
    if type(n) != int:
        print "error: wrong type"
        return
    if n == 0:
        return 1
    elif n > 0:
        print "at level n = ", n
        return n*factorial(n-1)
    else:
        print "error: negative integer"

def loopfactorial(n):
    # this if statement represents a complicated
    # logical test, with "short circuit evaluation"
    if type(n) != int or n < 0:
        print "error"
        return

    result = 1
    i = 1
    while i <= n:
        result = result*i
        i = i+1
        print "result = ", result

    return result
