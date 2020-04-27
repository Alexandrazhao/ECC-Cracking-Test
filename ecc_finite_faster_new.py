# Create a simple Point class to represent the affine points.
from collections import namedtuple
import time
import numpy as np
import random
from sympy import *


Point = namedtuple("Point", "x y")
point_list = []
# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
"NEED CHANGE"
p = 73
a = 0
b = 4



def gen_x(p):
    x = []
    low_bound = int(-(p-1)/2)
    upper_bound = int((p-1)/2)
    for i in range(low_bound, upper_bound+1):
        x.append(i)
    return x
    
def ecc_func(a, b, p):
    y_sqr_list = []
    for x in gen_x(p):
        y_sqr = x**3 + a*x +b
        y_sqr_list.append(y_sqr)
    return y_sqr_list

def residual(a,b,p):
    r_list = []
    for i in ecc_func(a,b,p):
        r = np.mod(i, p)
        r_list.append(r)
    return r_list

" determine if a single number is a quadratic residual"
"if is square, point + 2, if is 0, point + 1, if not square, not add"

def qua_residual(a,b,p,r):
    QR = 0
    for i in range(1,int(((p-1)/2)+1)): 
        if (i**2) % p == r :
            QR = 1
    if QR == 1:
        return 2
    elif r == 0:
        return 1
    else:
        return 0
            
#using if statement to determine how many points in an ecc field
def count_point(a, b, p):
    count = []
    for j in residual(a,b,p):
        count.append(qua_residual(a,b,p,j))
        
    return (sum(count)+1)

def divisor(n):
    possible_order = []
    for i in range(1, n+1):
        if n % i == 0:
            possible_order.append(i)
    return possible_order
    
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
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p-2, p)
"""
    Compute an inverse for x modulo p, assuming that x
    is not divisible by p.
"""

def ec_inv(P):
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

"find the started point in the initial"
def order_starter(R, m):
    "m is my upper bound"
    "now choose the order then go through, fix the number"
    "NEED CHANGE"
    order = order_p(0,4,73,57) 
    fix = None
    for i in range(1, order+1):
        if cons_p(i) == R:
            fix = i
    return fix
        
def break_ecc(F,m,n):
    i = order_starter(F,m)
    "NEED CHANGE"
    order = order_p(0,4,73,57)
    for j in range(i,m,order):

        if cons_p(j) == F and j == n:
            print(j, "yes")
            break

"F is the given point, m is the upper bound, n is the secret n, r is how many times"  
"I do this trial"
time_lapse = []
def time_inv(F, m, n, r):
    for i in range(r):
        cons_p(m)
        start = time.time()
        break_ecc(F,m,n)
        end = time.time()
        time_lapse.append(abs(end-start))
    return sum(time_lapse)/r
    
    

def order_p(a, b, p,num):
    cons_p(num)
    poss_list = divisor(count_point(a, b, p))
    for elem in poss_list:
        if cons_p(elem) == O :
            return elem
            break
    


"Generator point"
P = Point(0,2)
point_list.append(P)
pre_start = time.time()
cons_p(1000)
pre_end = time.time()
print("The pre calculation takes", pre_end-pre_start)
systemRandom = random.SystemRandom()
"cons_P(num of points(the group order), this is really important!!!!!!!!!)"
randomNumber = (systemRandom.randint(1,1000))
print(time_inv(cons_p(randomNumber),1000, randomNumber,1))
for i in range(100):
    randomNumber = (systemRandom.randint(1,1000))
    print(randomNumber, cons_p(randomNumber))
    print(time_inv(cons_p(randomNumber), 1000, randomNumber,1))




