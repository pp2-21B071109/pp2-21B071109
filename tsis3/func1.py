# 1)A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces.
#  ounces = 28.3495231 * grams
def func(grams):
    ounces = 28.3495231 * grams
    return ounces
gram = int (input())
print (func(gram))

#2) Read in a Fahrenheit temperature. Calculate and display the equival0ent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def temp(F):
    C = (5 / 9) * (F - 32)
    return C
f = float(input())
print(temp(F))

#3)Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads,numlegs):   
    chickens=0     
    rabbits=0          
    if(numlegs > numheads):         
        rabbits=(numlegs-2*numheads)/2         
        chickens=numheads-rabbits         
        return(int(chickens),int(rabbits))

numheads = int(input())
numlegs = int (input())
print(solve(numheads,numlegs))

#4) You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def filter_prime(num):
    prime = []
    a = 2
    for j in range(len(num)):
        if (num[j] == 1):
           pass
        elif (num[j] !=1 ): 
            while num[j] %a != 0:
                a+=1
            if (num[j] % 2 == 0 and num[j] !=2):
                pass
            elif (a == num[j]):
                prime.append(num[j])
    print(prime)
            
        
num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
filter_prime(num)


#5)Write a function that accepts string from user and print all permutations of that string.
import itertools 
def perms (s):
    perm_set = itertools.permutations(s) 
    for i in perm_set: 
        print(i)
s = input()
perms(s)


#6) Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def rev(s):
    s.reverse()
    print(' '.join(s))
s = input().split()
rev(s)
#7) Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for j in range(len(num)):
        a = False
        s = num[j]*10 +num[j-1]
        if (s ==33):
            a = True
        else:
            a = False
    return a
    
    
num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
print (has_33(num))
#8) Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(num):
    for j in range(2, len(num)):
        a = False
        b = num[j-2] *10 + num[j-1]*10 + num[j]
        if (b == 7):
            a = True
            break
    return a
    
    
num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
print (spy_game(num))
#9)Write a function that computes the volume of a sphere given its radius.
def func(r):
    vol = 4/3*r*r*r
    return vol    
    
    
r= int(input())
print(func(r))

#10)Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set. 
def notset(num):
    unique = []
    for i in num:
        if i not in unique:
            unique.append(i)
    return unique
    
num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
print(notset(num))


#11)Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def palindrome(s):
    d = []
    for i in range(len(s)):
        d.append(s[i])
    d.reverse()
    counter = 0
    for i in range(len(s)):
        if (s[i] == d[i]):
                counter+= 1 
    if (counter == len(s)):
        print ("palindrome")
    else :
        print("not palindrome")
            
s = input()
palindrome(s)

#12)Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def hist(num):
    for i in range(len(num)):
        res = '*' * num[i]
        print(res)

 

num = []
n = int(input())
for i in range (0 , n):
    number = int(input())
    num.append(number)
hist(num)

#13)Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
import random
user= input("Hello! What is your name?")
print("Well,", user ,",I am thinking of a number between 1 and 20.")
num = random.randint(1, 20)
guess = 0
counter = 0
while guess != num:
    print("Take a guess")
    guess = int(input())
    counter += 1
    if guess < num:
        print('Your guess is too low.')
    elif guess > num:
        print('Your guess is too high')
    else:
        print(f"Good job, {user}! You guessed my number in {counter} guesses!")
        break

#14)