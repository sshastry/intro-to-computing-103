# A permutation of a string s is a string t in which each character of s appears
# once and only once in t
# s = aab, then t = aba is a permutation.
# s = xyz, then t = zxy is a permutation.
#
# Problem:
# given a string, construct a list of all possible permutations of that string.
#
# Example:
# given ABC we want the list
# ['ABC','ACB','BAC','BCA','CAB','CBA']
#
# This reminds you of the recursive defn of factorial fact(n) is defined in terms
# of smaller factorials this suggests that the list of all permutations could be
# defined in terms of smaller permutations.
#
# To find all permutations of n objects:
# For a given object
# Find all permutations of n-1 objects
# Insert the given object into all possible positions
# of each permutation of n-1 objects
#
# Example: given ABC
# Find all permutations of BC
#   BC and CB
# Insert the remaining object A into all possible positions
# marked by a *, in each of the permutations of BC
#   *B*C* and *C*B*

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
