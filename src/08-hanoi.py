# We are given three pegs
# The first (source) peg holds a number of rings
# You want to move all rings to the last (destination) peg
# You can only move one ring at a time
# You can never put a larger ring on top of a smaller ring
# You have one auxiliary peg you can use
#
# Move the top n-1 rings from src to aux (recursively)
# Move the largest ring from src to dest
# Move the n-1 rings from aux to dest (recursively)
#
# Let us call our initial three pegs 'A', 'B', 'C' and
# initially all n rings are on 'A' and we want to move them to
# 'C'.

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
