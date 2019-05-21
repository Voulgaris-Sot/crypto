def frequency(text):
    l = [0 for x in xrange(26)]
    for c in text:
        l[ord(c)-ord('A')]+=1
    return l

def chi(c,e,N):
    chi_sum=0
    for i in xrange(0,26):
        e_i = N*e[i]
        chi_sum += ((c[i]-e_i)**2)/e_i

    return chi_sum

def decipher(text,key):
    l=''
    for letter in text:
        l += (chr(ord('A')+(ord(letter)-ord('A') - key)%26))
    return l

cipher_text = "TLXMYJPNHHGTPJMALVGCXDXYLNFHRBTHWPWJZNKHKZNUESCSZOGKXFEBXZXRCFXZWDTXGPKYEIYYETTMFHRUHUKALRENALFITAAAHRJVKLEBZZILETPUGKFIZNALVYZIWJEEYYOLVSPWHTIRCYTSMKJCULPZPPXALREOGHVDPXMYYKSUGKYENIGKMKTIGHPCZPXDMCWBTCIKSYYPRRWQHYH"

english_freq =[0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]

key_length = 6
columns = [cipher_text[i::key_length] for i in xrange(key_length)]

alphabet = map(chr, xrange( ord('A'), ord('Z')+1))

for l in columns:
    print l
    for i in xrange(0,25):
        print i,alphabet[i], chi(frequency(decipher(l,i)),english_freq,len(l))

