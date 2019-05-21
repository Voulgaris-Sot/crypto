import time

def mul(A,B):
    a,b,c=A
    d,e,f=B
    return a*d+b*e,a*e+b*f,b*e+c*f

def pow(A,n):
    if n==1:
        return A
    if n&1==0:
        return pow(mul(A,A),n//2)
    else:
        return mul(A,pow(mul(A,A),(n-1)//2))

def fib(n):
    if(n<2):
        return n
    return pow((1,1,0),n-1)[0]

start=time.clock()

for i in xrange(1,1000001):
    if(i % 1000000==0):
        print fib(i)
finish=time.clock()

print "Time elapsed",finish-start
