#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:54:56 2020

@author: yuxuanzhao
"""

# Create a simple Point class to represent the affine points.
from collections import namedtuple
import time
import random
Point = namedtuple("Point", "x y")
point_list = []
# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
p = 271
a = 0
b = 12

def valid(P):
    """
    Determine whether we have a valid representation of a point
    on our curve.  We assume that the x and y coordinates
    are always reduced modulo p, so that we can compare
    two points for equality with a simple ==.
    """
    if P == O:
        return True
    else:
        return (
            (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and
            0 <= P.x < p and 0 <= P.y < p)
        
        
def inv_mod_p(x):
    """
    Compute an inverse for x modulo p, assuming that x
    is not divisible by p.
    """
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p-2, p)

def ec_inv(P):
    """
    Inverse of the point P on the elliptic curve y^2 = x^3 + ax + b.
    """
    if P == O:
        return P
    return Point(P.x, (-P.y)%p)

def ec_add(P, Q):
    """
    Sum of the points P and Q on the elliptic curve y^2 = x^3 + ax + b.
    """
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid inputs")

    # Deal with the special cases where either P, Q, or P + Q is
    # the origin.
    if P == O:
        result = Q
    elif Q == O:
        result = P
    elif Q == ec_inv(P):
        result = O
    else:
        # Cases not involving the origin.
        if P == Q:
            dydx = (3 * P.x**2 + a) * inv_mod_p(2 * P.y)
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
        x = (dydx**2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        result = Point(x, y)

    # The above computations *should* have given us another point
    # on the curve.
    assert valid(result)
    return result

def cons_p(n):
    for i in range(n-1):
        new_P = ec_add(P, point_list[i])
        point_list.append(new_P)
    return point_list[n-1]

"n here should be secret"
def break_ecc(R, m, n):
    for i in range(m):
        if cons_p(i) == R and i == n:
            print(i, "yes")
            break #once hit the right value, break out 
            
    
time_lapse = []
def time_inv(P, m,n,r):
    for i in range(r):
        cons_p(m)
        start = time.time()
        break_ecc(P,m,n)
        end = time.time()
        time_lapse.append(abs(end-start))
    print("the average time lapse is:", sum(time_lapse)/r)
        
    
P = Point(2, 66)
point_list.append(P)
systemRandom = random.SystemRandom()


#set the number of trials, recording the cracking time for each trial
for i in range(20):
    randomNumber = (systemRandom.randint(1,5000))
    print(randomNumber, cons_p(randomNumber))
    time_inv(cons_p(randomNumber),5000, randomNumber,1)
 
