# Create a simple Point class to represent the affine points.
from collections import namedtuple
import time
import numpy as np
Point = namedtuple("Point", "x y")
point_list = []
# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
"NEED CHANGE"
p = 1223
a = 0
b = 8



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
    possible_order = []
    for i in range(1, n+1):
        if n % i == 0:
            possible_order.append(i)
    return possible_order
    #print(possible_order)

#divisor(28)
    
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
    #print( point_list)
    return point_list[n-1]

#cons_p(7)
"find the started point in the initial"
def order_starter(R, m):
    "m is my upper bound"
    "now choose the order then go through, fix the number"
    "NEED CHANGE"
    order = order_p(0,8,1223,1224)
    for i in range(1, order+1):
        if cons_p(i) == R:
            #print(i)
            return i
            #print(cons_p(i))
            #break

def break_ecc(F,m,n):
    "NEED CHANGE"
    i = order_starter(Point(x=823, y=1064),100)
    "NEED CHANGE"
    order = order_p(0,8,1223,1224)
    for j in range(i,m,order):
        #print(j)
        #print(j,cons_p(j))
        if cons_p(j) == F and j == n:
            print(j, "yes")
            

time_lapse = []
def time_inv():
    for i in range(1):
        cons_p(1000)
        start = time.time()
        break_ecc(Point(x=1, y=3),400,307)
        end = time.time()
        time_lapse.append(abs(end-start))
        #print(abs(end-start))
    print("the average time lapse is:", sum(time_lapse)/1)
    
    

def order_p(a, b, p,num):
    #point_list = cons_p(n)
    #print(cons_p(7))
    cons_p(num)
    poss_list = divisor(count_point(a, b, p))
    for elem in poss_list:
        if cons_p(elem) == O :
            #return elem
            #print(True)
            #print(elem, "True")
            return elem
            break
    
        

P = Point(1,3)
point_list.append(P)
"cons_P(num of points(the group order), this is really important!!!!!!!!!)"
#print(cons_p(1977))
#order_p(1,1,11,14)
"NEED CHANGE"
cons_p(1000)
#print(cons_p(777))
#print(cons_p(307))
"NEED CHANGE"
break_ecc(Point(x=823, y=1064),1000,777)
#print("my 1000th point is:", cons_p())

#print(cons_p(9))
#Q = Point(2, 4)
#R = Point(2, 3103)
#print("2P:", ec_add(P,P))
TwoP = ec_add(P, P)
#point_list.append(TwoP)
#print(point_list[1])
ThreeP = ec_add(TwoP, P)
#print("3P:", ThreeP)
#point_list.append(ThreeP)
#print(ec_add(point_list[1],P))
FiveP = ec_add(ThreeP,TwoP)
#print("5P:", FiveP)
#TenP = ec_add(FiveP, FiveP)
#print(TenP)

#break_ecc(Point(x=1, y=3),400,307)
#main()
#time_inv()

# Compute 4P two different ways.
#assert ec_add(P, ThreeP) == ec_add(TwoP, TwoP)
# Check the associative law.
#assert ec_add(P, ec_add(Q, R)) == ec_add(ec_add(P, Q), R)