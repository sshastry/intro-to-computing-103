def fib(n):
    if type(n) != int or n < 0:
        print "error"
        return

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1)+fib(n-2)
