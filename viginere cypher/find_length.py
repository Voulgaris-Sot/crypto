import collections

def calculate_IC(cipher_text):
    N        = len(cipher_text)
    freqs    = collections.Counter( cipher_text )
    alphabet = map(chr, xrange( ord('A'), ord('Z')+1))
    freqsum  = 0.0

    for letter in alphabet:
        freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

    return freqsum / ( N*(N-1) )

def calc(k,text):
    #create the columns for key_length = k
    l = [text[i::k] for i in xrange(k)]

    #calculate the ic for every column
    ic = [calculate_IC(text) for text in l]

    #return the average
    return sum(ic) / float(k)

def ic_cmp(a,b):
    if abs(a[1] - 0.065) < abs(b[1] - 0.065):
        return -1
    return 1

#cipher_text = "TLXMYJPNHHGTPJMALVGCXDXYLNFHRBTHWPWJZNKHKZNUESCSZOGKXFEBXZXRCFXZWDTXGPKYEIYYETTMFHRUHUKALRENALFITAAAHRJVKLEBZZILETPUGKFIZNALVYZIWJEEYYOLVSPWHTIRCYTSMKJCULPZPPXALREOGHVDPXMYYKSUGKYENIGKMKTIGHPCZPXDMCWBTCIKSYYPRRWQHYH"

cipher_text = "TLXMYJPNHHGTPJMALVGCXDXYLNFHRBTHWPWJZNKHKZNUESCSZOGKXFEBXZXRCFXZWDTXGPKYEIYYETTMFHRUHUKALRENALFITAAAHRJVKLEBZZILETPUGKFIZNALVYZIWJEEYYOLVSPWHTIRCYTSMKJCULPZPPXALREOGHVDPXMYYKSUGKYENIGKMKTIGHPCZPXDMCWBTCIKSYYPRRWQHYH"
print cipher_text
ic=[ (key_length,calc(key_length,cipher_text)) for key_length in xrange(1,50) ]
ic.sort(ic_cmp)
print(ic)
