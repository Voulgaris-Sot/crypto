def dec(text,key):
    plain_text = ""
    N = len(key)
    for i,letter in enumerate(text):
        plain_text += chr( ord('A') + ( ord(letter) - ord(key[i%N]))%26)
    return plain_text

cipher_text = "TLXMYJPNHHGTPJMALVGCXDXYLNFHRBTHWPWJZNKHKZNUESCSZOGKXFEBXZXRCFXZWDTXGPKYEIYYETTMFHRUHUKALRENALFITAAAHRJVKLEBZZILETPUGKFIZNALVYZIWJEEYYOLVSPWHTIRCYTSMKJCULPZPPXALREOGHVDPXMYYKSUGKYENIGKMKTIGHPCZPXDMCWBTCIKSYYPRRWQHYH"

key = "LUTHER"
plain_text = dec(cipher_text,key)
print plain_text
