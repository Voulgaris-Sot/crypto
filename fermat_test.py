from random import *

#fast modular exponentiation
def modexp ( a, u, n ):
    s = 1
    while u != 0:
        if u & 1:
            s = (s * a)%n
        u >>= 1
        a = (a * a)%n;
    return s

# n=The number to check,s=Number of iterations
def fermat(n,s):
    if(n<=1):
        return False
    if(n<=3):
        return True
    for i in xrange(s):
        #pick a random number to check the test
        a=randint(2,n-1)
        x=modexp(a,n-1,n)
        if x != 1:
            return False

    return True

carmi =[561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461]

for i in xrange  (1,11):
    n=pow(2,100*i)-1
    if fermat(n,40):
        print n," passes the test"

for n in carmi:
    if fermat(n,5):
        print n," passes the test"
