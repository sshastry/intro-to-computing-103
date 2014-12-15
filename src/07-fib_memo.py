# this definition procedure is extremely inefficient as it computes the same
# values over and over again needlessly.
def F(n):
    if type(n) != int or n < 0:
        print "error"
        return

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return F(n-1)+F(n-2)

# Let us define a global variable, a list memo which will store the previously
# calculated values of fib. We will use the fact that
# fib(n) > 0 for all n > 0
# We need to initialize the memo list to be zeroes, up to some predefined maximum
# value, so we are not allowed to compute fib(N) for N > MAX.
#
# this technique is called "dynamic programming" or "memoization"

MAX = 1000
memo = MAX * [0]
memo[0] = 0
memo[1] = 1

def fib(n):
    # this is the logical test which tells us
    # whether or not we've already computed fib(n)
    # and therefore saves us from redundant
    # computation
    if n == 0 or n == 1 or memo[n] > 0:
        return memo[n]

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
