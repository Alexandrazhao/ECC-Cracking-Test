#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:54:22 2020

@author: yuxuanzhao
"""
from functools import reduce
import random
import math
import time



#print(lcm(60,52))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
        
#print(prime_factors(3233))

def get_phi(p,q,n):
    list = prime_factors(n)
    p = list[0]
    q = list[1]
    phi = (p-1)*(q-1)
    return phi


def lcm(n):
    a = prime_factors(n)
    p = a[0]-1
    q = a[1]-1
    #print(p)
    return abs(p*q) // math.gcd(p, q)


#print(lcm(3233)) 
                
    
#a and n are two public keys
def multiplicative_inverse(a, n):
    m = lcm(n)
    #print(m)
    for x in range(1, m):
        if ((a*x)%m == 1):
            return x
    return 1


#print(multiplicative_inverse(5,6))

time_lapse = []

def time_inv(e, m):
        for i in range(1):
            start = time.time()
            multiplicative_inverse(e, m)
            end = time.time()
            time_lapse.append(abs(end-start))
        print("the average time lapse is:", sum(time_lapse)/1)
        print(multiplicative_inverse(e,m))
        
time_inv(25479136799,21990360151)
    
    



        

        
