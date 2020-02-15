#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:13:53 2019

@author: yuxuanzhao
"""

import random
import math
'''using Euclid's algorithms to determine gcd
'''
'''
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    print(a)
    return a
'''

print(math.gcd(20186,9827))
# mulriplicative inverse of two numbers

def multiplicative_inverse(a, b):
    #returns a tuple (r, i, j) such that r = gdc(a, b) = ia + jb
    
    # r = gcd(a, b) i = multiplicative_inverse of a mod b or j = multoplication_inverse 
    # of b mod a
    x = 0
    y = 0
    lx = 1
    ly = 0
    init_a = a
    init_b = b
    while b != 0:
        q = a // b
        (a, b) = (b, a%b)
        (x, lx) = ((lx-(q*x)), x)
        (y, ly) = ((ly-(q * y)), y)
    if lx < 0:
        lx = init_b +1  
    if ly < 0:
        ly = init_a +1
    # return a, lx, ly
    return lx


'''
def multiplicative_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a*x)%m == 1):
            return x
    return 1
'''
'''
def multiplicative_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while(a>1):
        q = a//m #q is a quotient
        t = m
        # m is a remainder now, process same as Euclid's algo
        m = a%m
        a = t
        t = y
        #update x and y
        y = x-q*y
        x = t
    #make x positive
    if (x< 0):
        x = x+m0
    return x
'''
print("the multi-inverse value is ", multiplicative_inverse(9,17))

''' test if a number is prime'''

def is_prime(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <=1:
        return False
    sqr = int(math.sqrt(a)) +1
    for divisor in range(3, sqr, 2):
        #print(divisor)
        if a % divisor == 0:
            return False
    return True

print(is_prime(17))

print(is_prime(198287318282838102837198236239999991919191919192827382919172823))

def generate_key(p, q):
    # first testify if p q are prime numbers
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p, q need to be both primes")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    m = p*q
    phi = (p-1)*(q-1)
    # choose a number e which is coprime with phi
    e = random.randint(1, phi)
    #use Euclid's Algorithm to verify that e and phi are coprime
    g = math.gcd(e, phi)
    while g !=1:
        e = random.randint(1, phi)
        g = math.gcd(e, phi)
        
    #generate the private key
    d = multiplicative_inverse(e, phi)
    print(d)
    print((e, m), (d, m))
    return ((e, m), (d, m))
    # return the public key(e, m) and the private key(d, m)
    #return ((e, m), (d, m))
    #print("public key is ", (e, m))
    #print("private key is", (d, m))

#generate_key(,13)

def encrypt(pk, text):
    # unpack the pk into key and m
    key, n = pk
    # convert each letter in text to numbers based on the character using a^b mod m
    cipher_text = [(ord(char)**key) % n for char in text]
    #return the array of bytes
    return cipher_text
#message = input("hello world")
#encrypt((121,143) , message)
def decrypt(pk, encode_text):
    #unpack the pk into key and m
    key, n = pk
    #using a^b mod m to gemerate text
    init_text = [chr((char**key) % n) for char in encode_text]
    return ''.join(init_text)

'''
if __name__ == '__main__':
    print ("RSA Encrypter / Decrypter")
    p = int(input("Enter a prime number"))
    q = int(input("enter another prime number"))
    print("Generate your public/private keypairs now")
    public, private = generate_key(p, q)
    print("Your public key is ", public , "Your private key is", private)
    message = input("ENter a message to encrypt with your private key")
    encode_msg = encrypt(private, message)
    print("Your encode message is : ")
    print(''.join(map(lambda x:str(x), encode_msg)))
    print(encode_msg)
    #print("Decrypting message with public key ", public, "...")
    #print("Your message is:")
    #print(decrypt(public, encode_msg))
'''
    


