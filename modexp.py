#http://eli.thegreenplace.net/2009/03/21/efficient-integer-exponentiation-algorithms/
#http://eli.thegreenplace.net/2009/03/28/efficient-modular-exponentiation-algorithms

def modexp_rl(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b /= 2
        if b == 0:
            break
        a = a * a % n

    return r

def _bits_of_n(n):
    """ Return the list of the bits in the binary
        representation of n, from LSB to MSB
        """
    bits = []

    while n:
        bits.append(n % 2)
        n /= 2

    return bits

def modexp_lr(a, b, n):
    r = 1
    for bit in reversed(_bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    return r

print modexp_rl(3,12,4)
print modexp_lr(3,12,4)

