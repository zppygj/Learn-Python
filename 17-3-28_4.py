# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:38:35 2017

@author: AYEAH
"""

#4.1 slice

a = list(range(100))
a[10:20] #11-20
a[:10:2] #every 2
a[::5] #every 5 

 #4.2 Iteration
 b = {'a':'1','b':'2','c':'3'}
 for key in b:
     print(key)
 for key,v in b.items():
     print(key,v)
     
for i in 'ABC':
    print(i)
    
from collections import Iterable
isinstance(b,Iterable)

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,2),(2,3),(4,5)]:
    print(x,y)

#4.3 list comprehensions

[x*x for x in range(1,10) if x%2==1]
[m +n for m in 'ABC' for n in 'xyz']

[k+'='+v for k,v in b.items()] #TypeError: must be str, not int

L = ['Word','Is','Mine']
[s.lower() for s in L]

L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L if isinstance(s,str)]
 
#4.4 generator
def odd():
    print('step 1')
    yield 2
    print('step 2')
    yield 3
    print('step 3')
    yield 5

a = odd()
next(a)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(8):
    print(i)
 
    
def f():
    n=1
    l=[1]
    while 1:
        if n==1:
            n=2
            yield l
        if n==2:
            n=3
            l=[1,1]
            yield [1,1]
        l=map(lambda x,y:x+y,l[0:n-2],l[1:])
        l=[1]+list(l)+[1]
        n+=1
        yield l 


n=0   
for i in f():
    print(i)
    if n>5:
        break
    n=n+1
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 