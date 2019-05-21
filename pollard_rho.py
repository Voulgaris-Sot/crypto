#implementation of pollard-rho factorization
from fractions import gcd
from random import randint

def pollardRho(n):
    i=1
    x=y=2
    print "i=%d x=%d y=%d" %(i,x,y)
    while True:
        i += 1
        x = (x*x-1)%n
        y = (y*y-1)%n
        y = (y*y-1)%n
        d = gcd(abs(y-x),n)
        print "i=%d x=%d y=%d d=%d" %(i,x,y,d)
        if( d!=1 ):
            print d
            break
        if( d==n):
            x=randint(2,n)
            y=x

def pollardRho_slow(n):
    i=1
    x=y=k=2
    print "I=%d x=%d y=%d" %(i,x,y)
    while True:
        i += 1
        x = (x*x -1)%n
        d = gcd(abs(y-x),n)
        print "I=%d x=%d y=%d d=%d" %(i,x,y,d)
        if( (d!=1) and (d!=n) ):
            print d
            break
        if( i==k ):
            y = x
            k = 2*k

n=1039*1009
print n
pollardRho(n)

n=2111*2903
print n
pollardRho(n)

n=9439*9011
print n
pollardRho(n)

n=9127*7883
print n
pollardRho(n)

n=1069*9887
print n
pollardRho(n)

n=2003*9973
print n
pollardRho(n)

n=1009*104729
print n
pollardRho(n)

n=1009*101273
print n
pollardRho(n)

n=101999*101273
print n
pollardRho(n)

#print "SLOW",n
#pollardRho_slow(n)

