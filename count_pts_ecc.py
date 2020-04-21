#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:45:41 2020

@author: yuxuanzhao
"""
"only works for prime numbers"

import numpy as np
import math

def gen_x(p):
    x = []
    low_bound = int(-(p-1)/2)
    upper_bound = int((p-1)/2)
    for i in range(low_bound, upper_bound+1):
        x.append(i)
    return x
    #print(x)
    

def ecc_func(a, b, p):
    y_sqr_list = []
    for x in gen_x(p):
        y_sqr = x**3 + a*x +b
        y_sqr_list.append(y_sqr)
    #print(y_sqr_list)
    return y_sqr_list

def residual(a,b,p):
    r_list = []
    for i in ecc_func(a,b,p):
        r = np.mod(i, p)
        r_list.append(r)
    #print(r_list)
    return r_list

" determine if a single number is a quadratic residual"
"if is square, point + 2, if is 0, point + 1, if not square, not add"

def qua_residual(a,b,p,r):
    QR = 0
    for i in range(1,int(((p-1)/2)+1)): 
        if (i**2) % p == r :
            QR = 1
            #return 1
    if QR == 1:
        return 2
        #print(1)
    elif r == 0:
        return 1
        #print(0)
    else:
        return 0
        #print(-1)
            
#using if statement to determine how many points in an ecc field
def count_point(a, b, p):
    #count = 0
    count = []
    for j in residual(a,b,p):
        count.append(qua_residual(a,b,p,j))
        '''
        if qua_residual(a,b,p, j) == 1:
            count = count+2
        elif qua_residual(a,b,p, j) == 0:
            count = count+1
        else:
            count = count+0
        '''
    return (sum(count)+1)
    #print(sum(count)+1)
    #return count
'''
def outcome():
    for x in len(p):
        if qua_residual(a,b,p) == 1:
'''
def divisor(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
            
#divisor(count_point(1,1,11))


print(count_point(0,1,109))
#qua_residual(0,11,7,0)


'''This part is new for y^2 = x^3+b mod m, where b<= m, to see the characteristic of the field'''
degree_list = []
def count_degree(a,p):
    for i in range(p):
        degree_list.append(count_point(0,i,p))
    return degree_list

print(count_degree(0,19 ))

'''function to check log base 2'''
def log2(x):
    if x == 0:
        return False
    return (math.log10(x) / math.log10(2))
'''function to check log base 3'''
def log3(x):
    if x == 0:
        return False
    return (math.log10(x) / math.log10(3))

def isPowerOfThree(n):
    if ( math.ceil(log3(n))==math.floor(log3(n))):
        return True
    else:
        return False


def isPowerOfTwo(n):
    if ( math.ceil(log2(n))==math.floor(log2(n))):
        return True
    else:
        return False
    
#print(isPowerOfTwo(10))

def find_power_two():
    for j in degree_list:
        #print(j)
        if (isPowerOfTwo(j)):
            print(j, "yes")
        elif (isPowerOfThree(j)):
            print(j, "yes")
            
find_power_two()
            



    




    