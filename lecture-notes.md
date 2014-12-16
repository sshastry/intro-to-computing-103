
## equality vs assignment

The point is that in python `a = b` is an assignment and `a == b` is a statement of equality.

In mathematics `a = b` is a statement of equality, and `let a = b` is an assignment.

## ipython

In ipython you can get a lot of mileage by just experimenting with tab, ?, and ??.

```
In [2]: s = 'hello'

In [3]: s.<tab>
s.capitalize    s.isalpha       s.ljust         s.rstrip
s.center        s.isdecimal     s.lower         s.split
s.count         s.isdigit       s.lstrip        s.splitlines
s.encode        s.isidentifier  s.maketrans     s.startswith
s.endswith      s.islower       s.partition     s.strip
s.expandtabs    s.isnumeric     s.replace       s.swapcase
s.find          s.isprintable   s.rfind         s.title
s.format        s.isspace       s.rindex        s.translate
s.format_map    s.istitle       s.rjust         s.upper
s.index         s.isupper       s.rpartition    s.zfill
s.isalnum       s.join          s.rsplit

In [5]: s.find?
Type:       builtin_function_or_method
String Form:<built-in method find of str object at 0x1f878f0>
Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
```

Suppose that this is the file `crawl_str.py`

```python
s = """
<html>
<body>
This is a test page for learning to crawl!
<p>
It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a>
before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.
</p>
</body>
</html>
"""
```

Then we can load it into the interpreter with `ipython -i crawl_str.py` or
`python -i crawl_str.py`.

## mutable vs immutable

If we write
```python
L = [1,2,3]
```
then we can think of the name L is an arrow pointing to an object in (a
Platonic) space holding `[1,2,3]`. If we execute
```python
L[1] = 100
```
then `L` is `[1,100,3]`

If we execute `M = L` then `M` is an arrow to the same object in space.
Therefore a change to `M[1]` is a change to the object in space, and therefore
that change is reflected in `L`.

However if we write
```python
L = L + [4,5,6]
```
then `L` becomes an arrow to a new object in space.

This is a convention of python, that reaching into the index of the list
changes the object in space, but any other operation on the list creates a new
list.

Now consider
```python
s = 'hello'
t = s
```
what has happened is that
```
s = 'hello' # created a new object in space
t = s # points to that same object in space
t = 'goodbye' # makes t point to a new object in space
```

The point to remember: the operation of indexing
```python
L[i]
```
reaches into space

but other operations such as `L = L + [10]`, create a new object in space.

Therefore the behavior of an operation reflects the fact of whether or not it
modifies the object in space or it creates a new object.

Always ask when doing an operation of any kind on a variable x, "Am I modifying
the object in space, or am I creating a new object?"

## for and while loops

```python
In [38]: while x < 0:
   ....:     print x
   ....:     x = x + 1
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

def nthLetter_nTimes(s):
    L = list(s)
    M = []
    i = 1
    for y in L:
        M.append(i*y)
        i = i + 1

    return M

In [1]: nthLetter_nTimes('hello')
Out[1]: ['h', 'ee', 'lll', 'llll', 'ooooo']
```

## the algebra of boolean values

Recall from last week: one always has to ask "Am I creating a new object, or am
I modifying an existing object?"

We can also do
```python
x = -10
(x < 0) and (x < -1)
True

'abc'+'xyz'
'abcxyz'
```
so we can do "algebraic" operations not only on numbers but also on strings and
`{True, False}` in the sense that `and` looks like multiplication on booleans
and `+` looks like addition on strings.

## more on while loops

```python
while expr:
    block
```

* if expr is a true false expression then block is executed when expr is true
* if expr is a list then block is executed when expr is nonempty
* if expr is a number then block is executed when expr is nonzero
* if expr is a string then block is executed when expr is nonempty

## the greatest element of a list

```python
def sup(l):
    max = l[0]
    for x in l:
        if x > max:
            max = x
    return max
```

`sup` stands for "supremum" which is another way of saying "greatest".

## destructuring

By destructuring we mean that we're introducing variable names while unpacking
a more complicated structure.

```python
In [1]: l = []

In [2]: for i in range(5):
   ...:     l.append( [i,i+1,i+2] )
   ...:

In [8]: l
Out[8]: [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

In [9]: for [x,y,z] in l:
   ...:     print x, "plus one is", y
   ...:     print x, "plus two is", z
   ...:
0 plus one is 1
0 plus two is 2
1 plus one is 2
1 plus two is 3
2 plus one is 3
2 plus two is 4
3 plus one is 4
3 plus two is 5
4 plus one is 5
4 plus two is 6
```

Here is a more complicated example, from homework 3 of the udacity course.

```python
udacious_univs = 'Udacity',90000,0
usa_univs = [ ['California Institute of Technology',2175,37704],
['Harvard',19627,39849],
['Massachusetts Institute of Technology',10566,40732],
['Princeton',7802,37000],
['Rice',5879,35551],
['Stanford',19535,40569],
['Yale',11701,40500] ]

def total_enrollment(l):
    total_students = 0
    total_fees = 0
    for [univ,students,fees] in l:
        total_students = total_students + students
        total_fees = total_fees + fees

    return total_students, total_fees
```

Note the line
```python
    for [univ,students,fees] in l:
```
In earlier languages such as Java or C++, doing the same thing would take
considerably more code.

## recursion

Reference: Think Python sections
* 5.8 Recursion
* 6.5 More recursion
* 11.5 Memos

(1) In mathematics, the factorial function n! is defined by
```
0! = 1
n! = n*(n-1)!
```
and is undefined for negative integers. In python:

```python
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
```

(2) Can we define addition itself recursively?
```
n + m
+(n,m)
add(n,m)
```

If we knew how to add one to an integer, we could use that as the base case of
the recursion.

```python
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
```

(3) Can we recursively find the maximum of a list? How about with a loop:

```python
def destructiveloopfindmax(L):
    # assume that L is a list of positive integers

    max = 0
    while L:
        t = L.pop()
        if t > max:
            max = t

    return max

def nondestructiveloopfindmax(L):
    # just assume that L is a list of positive integers

    max = 0
    n = len(L)
    i = 0
    while i < n:
        if L[i] > max:
            max = L[i]
        i = i+1

    return max
```
(We forgot to find a recursive version!)

(4) Can we define the fibonacci numbers recursively? Yes, the mathematical
definition is recursive.

```
F(0) = 0
F(1) = 1
F(i) = F(i-1) + F(i-2)
```

```python
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
```

This is correct but it performs very slowly. We'll try to make it run faster in
the next lecture.

## more on recursion

The following definition is extremely inefficient as it computes the same
values over and over again needlessly.

```python
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
```

Let us define a global variable, a list `memo` which will store the previously
calculated values of fib. We will use the fact that
> fib(n) > 0 for all n > 0
We need to initialize the memo list to be zeroes, up to some predefined maximum
value and therefore we cannot call `fib(N)` for `N > MAX`.

This technique is called "dynamic programming" or "memoization."

```python
MAX = 1000
memo = MAX * [0]
memo[0] = 0
memo[1] = 1

def fib(n):
    # this is the logical test which tells us whether or not we've already
    # computed fib(n) and therefore saves us from redundant computation
    if n == 0 or n == 1 or memo[n] > 0:
        return memo[n]

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

## The Towers of Hanoi

We are given three pegs
* The first (source) peg holds a number of rings
* You want to move all rings to the last (destination) peg
* You can only move one ring at a time
* You can never put a larger ring on top of a smaller ring
* You have one auxiliary peg you can use

The algorithm to solve this problem is:
* Move the top n-1 rings from src to aux (recursively)
* Move the largest ring from src to dest
* Move the n-1 rings from aux to dest (recursively)

Let us call our initial three pegs 'A', 'B', 'C' and suppose that initially all
n rings are on 'A' and our goal is to move them to 'C'.

```python
def hanoi(n, src, aux, dest):
    if n == 0:
        return
    # move the top n-1 rings from src to aux using the dest
    # peg as a temporary storage
    hanoi(n-1, src, dest, aux)
    # move the bottom most peg from the src to the dest
    print src, '->', dest
    # move n-1 rings now on aux to the dest using the src
    # peg as a temporary storage
    hanoi(n-1, aux, src, dest)

hanoi(4, 'A', 'B', 'C')
```
Now let's try a more complicated recursion which produces all permutations of a
given string.

A permutation of a string s is a string t in which each character of s appears
once and only once in t. Examples:
* if s = aab, then t = aba is a permutation.
* if s = xyz, then t = zxy is a permutation.

Problem:
> given a string, construct a list of all possible permutations of that string.

Example: given ABC we want our function to return the list
```
['ABC','ACB','BAC','BCA','CAB','CBA']
```

This should remind you of how the recursive definition of factorial fact(n) is
defined in terms of smaller factorials. This suggests that the list of all
permutations could be defined in terms of smaller permutations.

To find all permutations of n objects:
* Fix one of the n objects, let's call it alpha
* Find all permutations of n-1 other objects
* Insert the alpha into all possible positions of each permutation of n-1
  objects

Example:
* given ABC
* all permutations of BC are [BC, CB]
* Insert the remaining object A into all possible positions marked by a `*`, in
  each of the permutations of BC: `*B*C*` and `*C*B*`

```python
def insert_at_all_positions(c, t):
    l = []
    for j in range(len(t)+1): # + 1 for the rightmost spot
        l.append(t[:j]+c+t[j:])
    return l

# let us try this out in the example

insert_at_all_positions('A', 'BC') # ['ABC', 'BAC', 'BCA']
insert_at_all_positions('A', 'CB') # ['ACB', 'CAB', 'CBA']

# now we have to put together all of these solutions

def permutations(s):
    result = []
    if len(s) == 1:
        result.append(s)
        return result
    else:
        first = s[0]
        rest = s[1:]
        simpler = permutations(rest)
        for p in simpler:
            additions = insert_at_all_positions(first,p)
            result = result + additions
        return result
```

## timing your code (also known as profiling)

```python
import time

def time_execution(code):
    # start the clock
    start = time.clock()
    # evaluate any string as if it is a Python command
    result = eval(code)
    # find difference in start and end time
    run_time = time.clock() - start
    # return the result of the code and time taken
    return result, run_time

time_execution("2+2")

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

spin_loop(10**6)
spin_loop(10**7)

time_execution("spin_loop(10**6)") # 0.08s
time_execution("spin_loop(10**7)") # 0.8s
time_execution("spin_loop(10**8)") # 8s

def hanoi_(n, src, aux, dest):
    if n == 0:
        return
    hanoi_(n-1, src, dest, aux)
    # print src, '->', dest # we only want to time it, not print the answers
    hanoi_(n-1, aux, src, dest)

hanoi(4, 'A', 'B', 'C')
hanoi_(4, 'A', 'B', 'C')

time_execution("hanoi_(4, 'A', 'B', 'C')")
time_execution("hanoi_(20, 'A', 'B', 'C')") # 0.43s
time_execution("hanoi_(21, 'A', 'B', 'C')") # 0.86s
time_execution("hanoi_(22, 'A', 'B', 'C')") # 1.71s
time_execution("hanoi_(23, 'A', 'B', 'C')") # 3.43s
```

## dictionaries

### Example Program: Word Frequency

Let's write a program that analyzes text documents and counts how many times
each word appears in the document.  This kind of analysis is sometimes used to
measure the similarity between two documents.

We will use a dictionary counts with keys the words in the document and values
the number of times the word appears in the document.

```python
f = open('rfc2822.txt', 'r')
text = f.read()
f.close()
```
There is one small complication with using a dictionary here. The first time we
encounter a word, it will not yet be in counts. Attempting to access a
non-existent key produces an error. To guard against this, we need a decision
in our algorithm which looks like this:
```
if w is already in counts:
    add one to the count for w
else:
    set count for w to 1
```
Our first task is to split our text document into a sequence of words. In the
process, we will also convert all the text to lowercase (so occurrences of
"Foo" match "foo") and eliminate punctuation (so "foo," matches "foo"). Here's
the code to do that:
```python
# convert all letters to lower case
text = text.lower()

# replace each punctuation character with a space
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    text = text.replace(ch, ' ')

words = text.split()

counts = {}
for w in words:
    if counts.has_key(w):
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
```

The last step is to print a report that summarizes the contents of counts. One
approach might be to print out the list of words and their associated counts in
alphabetical order.

```python
# get list of words that appear in document
uniqueWords = counts.keys()

# put list of words in alphabetical order
uniqueWords.sort()

# print words and associated counts
for w in uniqueWords:
    print w, counts[w]
```

For a large document, this won't be useful. There will be too many words, most
of which only appear a few times. More interesting is to print out the counts
for the n most frequent words in the document.

```python
items = counts.items()

# this doesn't give what we want, which is a ranking by the number of times a
# word appears.
items.sort()

# Type:       builtin_function_or_method
# String Form:<built-in method sort of list object at 0x2a5f170>
# Docstring:
# L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
# cmp(x, y) -> -1, 0, 1

# what we need to do is pass in a custom comparison function.

# cmp(a,b) returns -1 if a precedes b, 0 if they are the same, and 1 if a
# follows b. Here are a few examples.

cmp(1,2)
cmp("a","b")
cmp(3,1)
cmp(3.1,3.1)

def compareItems((w1,c1), (w2,c2)):
    if c1 > c2:
        return -1
    elif c1 == c2:
        return cmp(w1,w2)
    else:
        return 1

items.sort(compareItems)

# Then the top 10 most frequent words are
items[:10]
```
The function `compareItems` is known as a lexicographic order.

## list comprehensions

References for today's lecture:
* http://docs.python.org/tutorial/
* http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

In mathematics we can write the following:
```
S = { x*x for x in {0,1,...,9} }
V = {1, 2, 4, 8,..., 1024}
M = { x : x in S and x is even }
```
In mathematics these are called set comprehensions, and the notation is
sometimes called set builder notation. In python we can write the following:
```python
S = [x**2 for x in range(10)]
V = [2**i for i in range(11)]
M = [x for x in S if x % 2 == 0]
```
These are called list comprehensions.

Python does have sets and set comprehensions as well, but I won't discuss
these. We've already covered the difference between sets and lists.

Let's just do a lot of examples and compare with the equivalent code written in
terms of loops.

```python
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
```

### Nested List Comprehensions

The initial expression in a list comprehension can be any arbitrary expression,
including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists
of length 4:

```
matrix = [ [1,  2,  3,  4],
           [5,  6,  7,  8],
           [9, 10, 11, 12] ]
```

The following list comprehension will transpose rows and columns:
```python
[[row[i] for row in matrix] for i in range(4)]
```
This example is equivalent to:
```python
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
```
which, in turn, is the same as:

```python
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
```

Another example:
```python
words = "The quick brown fox jumps over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
```

### The Sieve of Eratosthenes

A prime number is a natural number which has exactly two distinct natural
number divisors: 1 and itself.

To find all the prime numbers less than or equal to a given integer n by
Eratosthenes' method:

0. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
0. Initially, let p equal 2, the first prime number.
0. Starting from p, count up in increments of p and mark each of these numbers
   greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.;
   note that some of them may have already been marked.
0. Find the first number greater than p in the list that is not marked. If
   there was no such number, stop. Otherwise, let p now equal this number
   (which is the next prime), and repeat from step 3.

When the algorithm terminates, all the numbers in the list that are not marked
are prime.

```python
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
```

## I/O and sorting algorithms

```python
# References:
#   Chapter 14 of Think Python
#   The Python 2.7.3 Tutorial on Input and Output
#   http://en.wikipedia.org/wiki/Bubble_sort
#   http://en.literateprograms.org/Merge_sort_(Python)

outfile = open('output.txt', 'w')
print outfile # <open file 'output.txt', mode 'w' at 0x........>

line1 = "abc def ghi\n"

outfile.write(line1)

for i in range(10):
    outfile.write(line1)

outfile.write("jkl mno pqr\n")
outfile.close()

# Let's look at formatting strings with the % operator.

camels = 42
str(camels)
'%d' % camels # this is the string 42, not the integer 42

# Using the % operator on strings, we use
# '%d' to format an integer
# '%g' to format a floating-point number
# '%s' to format a string

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

# Let's look now at the format method of strings.

'We are the {} who say "{}!"'.format('knights', 'Ni')

'{0} and {1}'.format('spam', 'eggs')

'{1} and {0}'.format('spam', 'eggs')

s = 'This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible')

'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')

import math
'The value of pi is approximately {}.'.format(math.pi)

# An optional ':' and format specifier can follow the field name. This allows
# greater control over how the value is formatted. The following example rounds
# Pi to three places after the decimal.

# Passing an integer after the ':' will cause that field to be a minimum number
# of characters wide.

'The value of pi is approximately {0:.3f}.'.format(math.pi)
'The value of pi is approximately {:.3f}.'.format(math.pi)
'The value of pi is approximately {x:.3f}.'.format(x=math.pi)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for key, value in table.items():
    print '{name:10} ==> {phone:10d}'.format(name=key, phone=value)
```

### Bubble sort

Bubble sort is a simple sorting algorithm that works by repeatedly stepping
through the list to be sorted, comparing each pair of adjacent items and
swapping them if they are in the wrong order.

```python
def bubblesort(l):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
    return l

bubblesort([3, 8, 0, 6, 7, 4, 2, 1, 9, 5])
```
### Mergesort

Here is a general pattern for solving problems recursively.  It doesn't always
work out so simply but this description is still useful.

> Divide the input into two pieces of equal size, solve the two subproblems on
> these pieces seperately by recursion, and then combine the two results into a
> complete solution.

We want to apply this principle to the problem of sorting as follows.

Suppose we had two sorted stacks of cards, say with numbers written on them. To
combine the two stacks into one we can proceed as follows. Each stack has the
smallest element on top. Whichever of the top values is the smallest is the
first element of the combined list.

Once the smaller card is removed, we look at the tops of the stacks again and
whichever is the smaller value will be the next item in the combined list. We
continue this process until both lists are exhausted. (This process is called
the "merging" of two sorted lists.)

Now that we know how to merge, we can apply the principle to sort a list of
numbers, nums:

```
mergesort nums:
    split nums into two halves
    mergesort the first half
    mergesort the second half
    merge the two sorted halves into a list result
    return result
```

```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result = result + left[i:]
    result = result + right[j:]
    return result

def mergesort(l):
    if len(l) < 2:
        return l
    middle = len(l)/2
    left = mergesort(l[:middle])
    right = mergesort(l[middle:])
    return merge(left, right)

mergesort([3, 8, 0, 6, 7, 4, 2, 1, 9, 5])
```

## introduction to object oriented programming

```python
# Reference: Think Python version 2.0.4, ch 15, 16, 17

class MyFirstClass:
    pass

class Point:
    pass

# The Point class has no data or behavior. We must add attributes.

p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6

print p1.x, p1.y
print p2.x, p2.y

# To assign a value to an attribute on an object we use the syntax
#
#       <object>.<attribute> = <value>

# Let's start again:

class Point:
    def reset(self):
        self.x = 0
        self.y = 0
    def increment(self):
        self.x = self.x + 1
        self.y = self.y + 1

p = Point()
p.reset()
print p.x, p.y

# defining a class method in python is just like defining a function, as in the
# case of reset.

# The difference between class methods and normal functions is that all methods
# must have one argument which is traditionally named self.

# The self argument is a reference to the object that the method is being called
# on. In the definition of

p.increment()
print p.x, p.y

q = Point()
q.reset()
for i in range(10):
    q.increment()
print q.x, q.y

# The definition of increment is the same for both p and q, but 'self' of
# q.increment() refers to q.x and q.y, and 'self' of p.increment() refers to p.x
# and p.y. The follwing would give an error:

# r = Point()
# print r.x, r.y

# We shouldn't have to call reset() explicitly, would like it to be
# done automatically. For this we require the class constructor called __init__

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def increment(self):
        self.x = self.x + 1
        self.y = self.y + 1

r = Point()
print r.x, r.y

# Note that class objects are mutable, like lists. Therefore we can change the
# values of r.x and r.y.

# The next thing to look at is operator overloading.

s = 'abc'
t = 'def'

# We're already familiar with s+t == 'abcdef'; our goal is to define a string
# made by crushing the list of all ordered pairs with one char from s and one
# char from t. Thus
#   s*t := 'adaeafbdbebfcdcecf'
# whether or not this is actually useful is another matter altogether.

class ProductString:
    def __init__(self, value):
        if isinstance(value, str):
            self.x = value
        else:
            return 'error'
    def __mul__(self, other):
        if isinstance(other, ProductString):
            s = ''
            for c in self.x:
                for d in other.x:
                    s = s + c + d
            return s
        else:
            return 'error'

s = ProductString('abc')
t = ProductString('def')
s*t

# Source: http://infohost.nmt.edu/tcc/help/lang/python/examples/rational/

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class Rational:
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError
        if b == 0:
            raise ZeroDivisionError
        else:
            g = gcd(a, b)
            self.n = a/g
            self.d = b/g
    def __add__(self, other):
        return Rational(self.n*other.d + other.n*self.d, self.d*other.d)
    def __sub__(self, other):
        return Rational(self.n*other.d - other.n*self.d, self.d*other.d)
    def __mul__(self, other):
        return Rational(self.n*other.n, self.d*other.d)
    def __div__(self, other):
        return Rational(self.n*other.d, self.d*other.n)
    def __str__(self):
        return str(self.n) + "/" + str(self.d)
    def __float__(self):
        return float(self.n)/float(self.d)

Rational(1,0) # ZeroDivisionError
Rational(2.5,2) # TypeError
Rational('a',2) # TypeError

third = Rational(1,3)
print third # 1/3
fifth = Rational(1,5)
print fifth # 1/5
print third + fifth # 8/15
print third * fifth # 1/15
print third-fifth # 2/15
print fifth/third # 3/5

print float(fifth) # 0.2
print float(third) # 0.333333333333

print Rational(50,100) # 1/2
```

