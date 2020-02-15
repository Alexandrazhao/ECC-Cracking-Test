from sympy import *
from numpy import *




#y = Symbol('y')
#m, a, b = symbols('m a b')
a = 0
b = 8
x = 1
y = 3
m_same = (3*(x**2)+a)/(2*y)
new = m_same**2-2*x
#print(new)
temp = -2*x + (a + 3*x**2)**2/(4*(x**3 + a*x + b))
#e_exp = expand(temp)
#x_sim = simplify(e_exp) #the simplified x expression
#print(x_sim) # the x coordinate of 2P
#x1 = (0**2/4 - 0*1**2/2 - 2*8*1 + 1**4/4)/(0*1 + 8 + 1**3)
x1 = m_same**2-2*x
print("x1 = ", x1) # the x coordinate
temp_y = y+m_same*(x1-x)
y1 = -temp_y
print("y1 = ", y1) # the y coordinate
#y_exp = expand(new_y)

m_diff = (y1-y)/(x1-x)
x2 = m_diff**2-x1-x
y2 = y+m_diff*(x2-x)

print("x2 = ", x2)
print("y2 = ", -y2)








y_temp=a**3/(8*a*x*y + 8*b*y + 8*(y**2-a*x-b)*y) + a**2*x**2/(8*a*x*y + 8*b*y + 8*(y**2-a*x-b)*y) - a*b*x/(a*x*y + b*y + (y**2-a*x-b)*y) - 5*a*x*(y**2-a*x-b)/(8*a*x*y + 8*b*y + 8*(y**2-a*x-b)*y) - a*x/(2*y) - 3*b*(y**2-a*x-b)/(a*x*y + b*y + (y**2-a*x-b)*y) + 3*((y**2-a*x-b)**2)/(8*a*x*y + 8*b*y + 8*(y**2-a*x-b)*y) - 3*(y**2-a*x-b)/(2*y) + y

y_sim = simplify(y_temp)
print(y_sim) # the y coordinate of 2P
y_cor = (0**3 + 9*0**2*1**2 + 27*0*8*1 - 3*0*1*3**2 + 27*8**2 - 18*8*3**2 - 3**4)/(8*3**3)
print(y_cor)
#3P is 2P + P, which requires the different point addition and one doubling
m_dist = (y-y_sim)/(x-x_sim)
#print("m_dist = ", m_dist)

x3 = m_dist**2 - x - x_sim
#exp_3 =expand(x3)
#print(exp_3)
#print(simplify(exp_3))

#print("x3 is", x3)
y3 = y+m*(x3-x)
#print("y3 is", y3)

#4P
m4 = (3*x_sim**2+a)/(2*y_sim)
x4 = m4**2 - 2*x_sim
#print("x4 is", x4)
y4 = y_sim+m4*(x4-x_sim)
#print("y4 is", y4)

'''
y_sim = simplify(y_temp)
y_sim1 = (a**3 + 9*a**2*x**2 + 27*a*b*x - 3*a*x*y**2 + 27*b**2 - 18*b*y**2 - y**4)/(8*y**3)
print(y_sim)
x1 = -0.409
y1 = 1.715
a1 = -1
b1 = 2.6
x2 = -2*x1 + (a1 + 3*x1**2)**2/(4*(x1**3 + a1*x1 + b1))
y2 = (a1**3 + 9*a1**2*x1**2 + 27*a1*b1*x1 - 3*a1*x1*y1**2 + 27*b1**2 - 18*b1*y1**2 - y1**4)/(8*y1**3)
print("the x for 2P is", x2)
print("the y for 2P is", y2)
x4 = -2*x2 + (a1 + 3*x2**2)**2/(4*(x2**3 + a1*x2 + b1))
y4 = (a1**3 + 9*a1**2*x2**2 + 27*a1*b1*x2 - 3*a1*x2*y2**2 + 27*b1**2 - 18*b1*y2**2 - y2**4)/(8*y2**3)
print("the x for 4P is", x4)
print("the y for 4P is", y4)
'''
