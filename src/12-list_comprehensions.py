# References for today's lecture:
# (1) http://docs.python.org/tutorial/
# (2) http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# In mathematics we can write the following:
#
# S = { x*x for x in {0,1,...,9} }
# V = {1, 2, 4, 8,..., 1024}
# M = { x : x in S and x is even }
#
# In mathematics these are called set comprehensions, also known as set builder
# notation.
#
# In python we can write the following:

S = [x**2 for x in range(10)]
V = [2**i for i in range(11)]
M = [x for x in S if x % 2 == 0]

# These are called list comprehensions.
#
# Python does have sets and set comprehensions as well, but I won't discuss
# these. We've already covered the difference between sets and lists.
#
# Let's just do a lot of examples and see the equivalent code using loops.

################################################################################

squares = []
for x in range(10):
    squares.append(x**2)

squares = [x**2 for x in range(10)]

################################################################################

def f(n):
    for i in range(n):
        print (n-i)*' ' + i*'T'

def printlist(l):
    for s in l:
        print s

def f(n):
    return [(n-i)*' ' + i*'T' for i in range(n)]

# >>> f(10)
#
#          T
#         TT
#        TTT
#       TTTT
#      TTTTT
#     TTTTTT
#    TTTTTTT
#   TTTTTTTT
#  TTTTTTTTT

################################################################################

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

################################################################################

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

################################################################################

# Nested List Comprehensions
#
# The initial expression in a list comprehension can be any arbitrary expression,
# including another list comprehension.

# Consider the following example of a 3x4 matrix implemented as a list of 3
# lists of length 4:

matrix = [ [1,  2,  3,  4],
           [5,  6,  7,  8],
           [9, 10, 11, 12] ]


# The following list comprehension will transpose rows and columns:

[[row[i] for row in matrix] for i in range(4)]

# This example is equivalent to:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

# which, in turn, is the same as:

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

################################################################################

words = "The quick brown fox jumps over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

################################################################################
#
# The Sieve of Eratosthenes
#
# A prime number is a natural number which has exactly two distinct natural
# number divisors: 1 and itself.
#
# To find all the prime numbers less than or equal to a given integer n by
# Eratosthenes' method:
#
# 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
#
# 2. Initially, let p equal 2, the first prime number.
#
# 3. Starting from p, count up in increments of p and mark each of these numbers
#    greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.;
#    note that some of them may have already been marked.
#
# 4. Find the first number greater than p in the list that is not marked. If
#    there was no such number, stop. Otherwise, let p now equal this number
#    (which is the next prime), and repeat from step 3.
#
# When the algorithm terminates, all the numbers in the list that are not
# marked are prime.

from math import sqrt
n = 1000

# first using loops

A = [True] * n

for i in range(2,int(sqrt(n))):
    if A[i] == True:
        for j in range(2*i, n, i):
            A[j] = False

# now all i such that A[i] == True are prime.

primes_ = []
for i in range(len(A)):
    if i > 1 and A[i] == True:
        primes_.append(i)

# now using list comprehensions

composites = [j for i in range(2, int(sqrt(n))) for j in range(2*i, n, i)]
primes = [x for x in range(2, n) if x not in composites]

# we can compress it into one long line, but this is bad
# coding style.

primes = [x for x in range(2, n) if x not in [j for i in range(2, int(sqrt(n))) for j in range(2*i, n, i)]]

primes_ == primes

