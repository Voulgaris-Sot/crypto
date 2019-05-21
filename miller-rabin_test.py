from random import *

def modexp ( a, u, n ):
    s = 1
    while u != 0:
        if u & 1:
            s = (s * a)%n
        u >>= 1
        a = (a * a)%n;
    return s

def miller_rabin(n, k=10):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x=modexp(a,d,n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
              return False
        return True


carmi = [   561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461]

for i in xrange  (1,10):
    n=pow(2,100*i)-1
    if miller_rabin(n,40):
        print n," passes the test"


for n in carmi:
    if miller_rabin(n,40):
        print n," passes the test"
