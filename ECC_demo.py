
#px, py are my generator point on the curve
point_list = []
#append the generator to my list 
point_list.append((1,3))
def point_add(a, b, px, py, qx, qy):
    #if ecc_fun(a, b, px, py ) == True and ecc_fun(a, b, qx, qy) == True:
    if px != qx and py != qy:
        g = point_one_R(px, py, qx, qy)
        round(g[0], 4)
        round(g[1], 4)
        return g
            #print(g)
    else:
        g = point_tan_R(a, b, px, py)
        round(g[0], 4)
        round(g[1], 4)
        return g
            #print(g)

    #else:
        #print("your input is invalid.")
        
#brutal force doing nP, which is P+(n-1)P
def cons_p(a,b,px,py,s):
    for i in range(s-1):
        qx = point_list[i][0]
        qy = point_list[i][1]
        new_g = point_add(a,b,px,py,qx, qy)
        #print("new_g", new_g)
        #round_g = (round(new_g[0], 8), round(new_g[1], 8))
        #print(round_g)
        point_list.append(new_g)
    return point_list
        
#this part need to develop as an recursion. 
def fast_np(a,b,px,py,s):
    half = int(s/2)
    half_index = int((s/2)-1)
    if s % 2 == 0:
        cons_p(a,b,px,py,half)[half_index]
        double_x = (cons_p(a,b,px,py,half)[half_index])[0]
        double_y = cons_p(a,b,px,py,half)[half_index][1]
        g = point_tan_R(a,b,double_x, double_y)
        return g
    '''
    elif s % 2 == 1:
        half_odd = int((s-1)/2)
        half_odd_index = int((s/2)-1)
        cons_p(a,b,px,py,half_odd)[half_odd_index]
        double_x = (cons_p(a,b,px,py,half_odd)[half_odd_index])[0]
        double_y = cons_p(a,b,px,py,half_odd)[half_odd_index][1]
        g = point_tan_R(a,b,double_x, double_y)
        point_one_R()
   '''
   
'''
def cons_4p():
    qx = point_list[1][0]
    qy = point_list[1][1]
    return point_add(-7, 10, 1,2,qx,qy)
'''
def point_one_R(px, py, qx, qy):
    m = (py-qy)/(px-qx)
    rx = m**2-px-qx
    ry = py+m*(rx-px)
    return rx, -ry
    
    #print(rx, -ry)

def point_tan_R(a, b, px, py):
    m = (3*(px**2)+a)/(2*py)
    rx = m**2-px-px
    ry = py+m*(rx-px)
    #print(rx, -ry)
    return rx, -ry

#point_tan_R(-7, 10, 1,2)
'''
def point_mult_R(s,p):
    for i in s:
        point
'''

def ecc_fun(a, b, x, y):
    if round(y**2,4) == round(x**3+a*x+b,4):
        #print("True")
        return True

g1 = point_add(0, 8, 1,3,1,3)
#point_list.append(g1)
#1000P, and print out the 1000th P
print(cons_p(0,8,1,3,5000)[4980])
#print(fast_np(0,8,1,3,1000))
#print((cons_p(0,8,1,3,2)[1])[0])



#the following is to calculate the n
def break_ecc(a, b, px, py):
    for i in range(5000):
        if (cons_p(a,b,px,py,i)[i-1]) == (1.8499811817018426, 3.487682328123232):
            print(cons_p(a,b,px,py,i)[i-1])
            #print(cons_p(a,b,px,py,i)[i-1])
            #print(cons_p(0,8,1,3,10)[9])
            print(i, "yes")
            break
        #print(i)
        #else:
            #print(cons_p(0,8,1,3,4)[3])
            #print(cons_p(a,b,px,py,i)[i-1])
            #print("no")
        

#print(cons_p(1001))
            
break_ecc(0,8,1,3)

'''
g2 = cons_p()
point_list.append(g2)
g3 = cons_4p()
point_list.append(g3)
print(point_list)
#cons_p()
print(point_list[1][0])'''
#print(g1)
#print(g2)
#print(point_list[9999])

#print(point_add(0,8,1,3,-0.678,2.767))

#print(point_list[4])
#print(point_list[3][0])
#print(point_list[3][1])
#point_R(1,2,3,4)
#ecc_fun(-7, 10, -3, 2)
#testfy(-7, 10,  )
#print(ecc_fun(-7, 10, -1, -4))
#print(ecc_fun(-7, 10, -3.16, -0.752))