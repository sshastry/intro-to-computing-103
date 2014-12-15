# Reference: Think Python version 2.0.4, ch 15, 16, 17

class MyFirstClass:
    pass

class Point:
    pass

# The Point class has no data or behaviors. We must add attributes.

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
