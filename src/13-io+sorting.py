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

# Bubble sort

# Bubble sort is a simple sorting algorithm that works by repeatedly stepping
# through the list to be sorted, comparing each pair of adjacent items and
# swapping them if they are in the wrong order.

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

# Mergesort
#
# Here is a general pattern for solving problems recursively.  It doesn't always
# work out so simply but this describes many problems.
#
#     Divide the input into two pieces of equal size, solve the
#     two subproblems on these pieces seperately by recursion, and
#     then combine the two results into a complete solution.
#
# Now we want to apply this principle to the problem of sorting as follows.
#
# Suppose we had two sorted stacks of cards, say with numbers written on them. To
# combine the two stacks into one we can proceed as follows. Each stack has the
# smallest element on top. Whichever of the top values is the smallest is the
# first element of the combined list.
#
# Once the smaller card is removed, we look at the tops of the stacks again and
# whichever is the smaller value will be the next item in the combined list. We
# continue this process until both lists are exhausted.
#
# This process is called the "merging" of two sorted lists.
#
# Now that we know how to merge, we can apply the principle to sort a list of
# numbers, nums:

# mergesort nums:
#     split nums into two halves
#     mergesort the first half
#     mergesort the second half
#     merge the two sorted halves into a list result
#     return result

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
