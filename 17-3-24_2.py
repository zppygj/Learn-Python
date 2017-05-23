# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:23:27 2017

@author: AYEAH
"""

#2.1 call function
#  http://docs.python.org/3/library/functions.html#abs

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    elif x >= 0:
        return x
    else:
        return -x
#2.2 definite function
import math
def quadratic(a,b,c):
    deta = b**2 - 4*a*c #**表示乘方
    if deta > 0:
        x1 = (-b - math.sqrt(deta))/(2 * a) 
        x2 = (-b + math.sqrt(deta))/(2 * a)
        return x1,x2
    elif deta == 0:
        x1 = -b /(2 * a)
        x2 = -b /(2 * a)
        return x1,x2
    else:
        return
print(quadratic(1,5,4))
#2.3 functional parameter

def add_end(L=None):
    if L==None:
        L=[]
    L.append('end')
    return L

def calc(number):#variable can be list or tuple
    sam = 0
    for x in number:
        sam = sam + x**2
    return sam
a = [1,2,3,4]
calc(a)

def calc(*number):#variable can be list or tuple
    sam = 0
    for x in number:
        sam = sam + x**2
    return sam
calc(1,2,3,4)
a = [1,2,3,4]
calc(*a)



    
def f1(a,b,c,*sv,**kw):  
    print('a=',a,'b=',b,'c=',c,'sv=',sv,'kw=',kw)

def f2(a,b,c,*, d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
a=[1,2,3]
extra={'name':'Jack','age':'18'}
f1(1,2,3,4,5,**extra)
f2(1,2,3,d='c',**extra)

#2.4 recursive function
def move(n,a='A',b='B',c='C'):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    