#1)Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

pattern = r'ab*'

s = input()

pas = re.search (pattern , s)
if pas is not None :
    print (pas)
else :
    print ("The string does not match the pattern.") 



#2)Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

pattern = r'ab{2,3}'

s = input()

pas = re.search (pattern , s)
if pas is not None :
    print (pas)
else :
    print ("The string does not match the pattern.") 

#3)Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

pattern = r"[a-z]+_"

s = input()

pas = re.search (pattern , s)
if pas is not None :
    print (pas)
else :
    print ("The string does not match the pattern.") 

#4) Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

pattern = r"[A-Z][a-z]+"

s = input()

pas = re.findall(pattern , s)
if pas is not None :
    print (pas)
else :
    print ("The string does not match the pattern.") 
#5)Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

pattern = r"a.*b$"

s = input()

pas = re.findall(pattern , s)
if pas is not None :
    print (pas)
else :
    print ("The string does not match the pattern.") 


#6) Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

s=input()

pas =re.sub("[ ,.]","|",s)
print(pas)

#7) Write a python program to convert snake case string to camel case string.
import re
a = input()
def snake_to_camel(l):
     v = re.findall("[a-z]+", a)
     h = ""
     for i in v:
         h += i[0].upper() + i[1 : len(i)]
     return h
print(snake_to_camel(a))


#8)Write a Python program to split a string at uppercase letters.
import re
a = input()
b = re.findall('[A-Z][^A-Z]*', a)
print(b)

#9)Write a Python program to insert spaces between words starting with capital letters.
import re

text = input()


pattern = re.sub(r"(\w)(\s)+([A-Z])", r"\1 \3",text)
print(pattern)

#10)Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(a):
     b = re.sub('([A-Z])', r'_\1', a)
     b = b.lower()
     b = re.sub('_+', '_', b)
     if b.startswith('_'):
         b = b[1:]
     return b
a =  input()
b = camel_to_snake(a)
print(b)