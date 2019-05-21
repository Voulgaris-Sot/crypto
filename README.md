# Cryptography
This repo contains various small scripts that are crypto related, that I wrote during the course of Cryptography in NTUA. The viginere decypher was an exercise for that class.

## Viginere decypher
The ciphertext is known to be encrypted using the viginere method. Find_length.py uses the index of coincidence(IC) to find the most probable length of the key. The partial output of this programm is:  
[(46, 0.0644927536231884), (30, 0.06666666666666668),  
(12, 0.06672113289760347), (6, 0.06721132897603486),  
(18, 0.06969696969696969), (27, 0.05952380952380953),  ...]   
Under the asssumption that the key is a small phrase the most probable length is 6.  
Find_key.py uses the chi-squared statistic to compare the distribution of each column shifted with the ceasar cipher(each column corresponds to a letter of the key) to the english language distribution. The number of shifts and the corresponding letter with the smallest chi-squared value is a letter of the key.   
Finally, we decode the cypher and it is a speech by Martin Luther King and the key is LUTHER.
