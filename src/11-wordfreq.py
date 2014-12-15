# Example Program: Word Frequency
#
# Let's write a program that analyzes text documents and counts how many times
# each word appears in the document.  This kind of analysis is sometimes used to
# measure the similarity between two documents.
#
# We will use a dictionary counts with keys the words in the document and values
# the number of times the word appears in the document.

f = open('rfc2822.txt', 'r')
text = f.read()
f.close()

# There is one small complication with using a dictionary here. The first time we
# encounter a word, it will not yet be in counts. Attempting to access a
# non-existent key produces an error. To guard against this, we need a decision
# in our algorithm.

# if w is already in counts:
#     add one to the count for w
# else:
#     set count for w to 1

# The first task is to split our text document into a sequence of words. In the
# process, we will also convert all the text to lowercase (so occurrences of
# "Foo" match "foo") and eliminate punctuation (so "foo," matches "foo"). Here's
# the code to do that:

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

# Our last step is to print a report that summarizes the contents of counts.
# One approach might be to print out the list of words and their associated
# counts in alphabetical order.

# get list of words that appear in document
uniqueWords = counts.keys()

# put list of words in alphabetical order
uniqueWords.sort()

# print words and associated counts
for w in uniqueWords:
    print w, counts[w]

# For a large document, this won't be useful. There will be too many words, most
# of which only appear a few times.  More interesting is to print out the counts
# for the n most frequent words in the document.

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
