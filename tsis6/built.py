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
def is_palindrome(word):
    word = word.lower()
    reversed_word = ''.join(reversed(word))
    if word == reversed_word:
        return True
    else:
        return False
word = input()
print(is_palindrome(word))