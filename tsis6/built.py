#1)Write a Python program with builtin function to multiply all the numbers in a list

"""
from functools import reduce

numbers = [2, 3, 4, 5, 6]

product = reduce(lambda x, y: x * y, numbers)

print("Product of all numbers:", product)
"""

#2)Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
"""
def func(s):
    upcnt = 0
    lowcnt = 0
    for i in s:
        if i.isupper() :
            upcnt +=1
        elif i.islower():
            lowcnt+=1
    print(f"Number of letters in uppercase {upcnt}")
    print (f"Number of letters in lowercase {lowcnt}")
s = input() 
func(s)
"""
#3)Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""
def is_palindrome(word):
    word = word.lower()
    reversed_word = ''.join(reversed(word))
    if word == reversed_word:
        return True
    else:
        return False
word = input()
print(is_palindrome(word))
"""

#4)Write a Python program that invoke square root function after specific milliseconds.
"""
import math
import time
def sqrt_after_ms(num, ms):
    time.sleep(ms/1000)
    return math.sqrt(num)

num = int(input())
ms = int(input())
result = sqrt_after_ms(num, ms)
print(f"Square root of {num} after {ms} milliseconds is {result}")
"""
#5)Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)

t1 = (True, True, True)
t2 = (True, False, True)
print(all_true(t1))
print(all_true(t2))
