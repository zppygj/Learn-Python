# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:13:58 2017

@author: AYEAH
"""
#3.1 reduce and map
from functools import reduce

def prod(L):
    def mutil(x,y):
        return x*y
    return reduce(mutil,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

a = 'happppppy'
a.index('ppy')

b = '123.323'
float(b)

b.split('.')

a.find('p')

def trans(s):
    def f1(a):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[a]
    def f2(x,y):
        return x*10+y
    s1 = s.split('.')[0]
    s2 = s.split('.')[1]
    s3 = reduce(f2,map(f1,s1))
    s4 = reduce(f2,map(f1,s2))
    return s3+s4/(10**len(s2))

def is_odd(n):
    return n % 2 == 1
list(filter(is_odd,[1,2,3,4,5,6,7]))


#4.2 filter
a = 'afsddf   sdfefewaf sdffse'

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


def is_palindrome(n):
    m = str(n)
    c = len(m)
    for i in range(c):
        if m[i-1] == m[-i]:
            return True
        else:
            return False
        i = i + 1
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#4.3 sorted
a='4334'
a[0]==a[-1]
a[1]
a[-1]
len(a)
print(range(1,1000))
range(1000)[23]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return str.lower(t[0])
    
L2 = sorted(L, key=by_name)
print(L2)
def by_score(t):
    return t[1]
L3 = sorted(L,key=by_score,reverse=True)
print(L3)

def by_len(t):
    return len(t[0])
L4=sorted(L,key=by_len)
print(L4)

L5 = sorted(L,key=lambda t:-len(t[0]))
print(L5)

