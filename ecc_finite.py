# Create a simple Point class to represent the affine points.
from collections import namedtuple
import time
Point = namedtuple("Point", "x y")
point_list = []
# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
p = 3571
a = 0
b = 8

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
    #return point_list
    return point_list[n-1]

#cons_p(100)

def break_ecc(R, m):
    for i in range(m):
        #print(cons_p(i))
        #print(i, cons_p(i))
        if cons_p(i) == R:
            print(i, "yes")
            print(cons_p(i))
            #break
        
        
time_lapse = []
def time_inv():
    for i in range(10):
        #cons_p(301)
        start = time.time()
        break_ecc(Point(x=121, y=2778),1500)
        end = time.time()
        time_lapse.append(abs(end-start))
        #print(abs(end-start))
    print("the average time lapse is:", sum(time_lapse)/10)
        
    



P = Point(1, 3)
point_list.append(P)
#print(cons_p(1477))
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
time_inv()

#break_ecc(Point(x=3110, y=605),50)

# Compute 4P two different ways.
#assert ec_add(P, ThreeP) == ec_add(TwoP, TwoP)
# Check the associative law.
#assert ec_add(P, ec_add(Q, R)) == ec_add(ec_add(P, Q), R)