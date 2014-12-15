def addone(n):
    return n+1

def add(n,m):
    if type(n) != int or type(m) != int or n <= 0 or m <= 0:
        print "error"
        return

    if m == 1:
        print n,"+1"
        return addone(n)
    elif m > 1:
        print "1+"
        return addone(add(n,m-1))
