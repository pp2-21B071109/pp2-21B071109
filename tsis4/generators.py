#Create a generator that generates the squares of numbers up to some number N.
import math

def mygen(N):
    a = 1
    while a <=N:
        yield a**2
        a+=1
"""    
N = int(input())
for i in mygen(N):
    print (i)

"""
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def mygen2(N):
    a = 0
    while a <=N:
        if a%2== 0 :
            yield f"{a},"
        a+=1
""""
N = int(input())
ans = ""
for i in mygen2(N):
    ans += i
print (ans)
"""

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def mygen3(N):
    a = 1
    while a <=N:
        if a%12 == 0:
            yield a
        a+=1
"""
N = int(input())
for i in mygen3(N):
    print (i)
"""
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a , b):

    while a <=b:
        yield a**2
        a+=1
"""
a = int(input())
b = int(input())
for i in squares(a , b):
    print (i)
"""

#Implement a generator that returns all numbers from (n) down to 0.
def mygen5(N):
    a = 0
    while  N != a:
        yield N
        N-=1
"""
N = int(input())
for i in mygen5(N):
    print (i)
"""