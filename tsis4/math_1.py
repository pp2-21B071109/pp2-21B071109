import math 

#Write a Python program to convert degree to radian.
degree = int (input())

radian = degree * math.pi/180
print (radian)

#Write a Python program to calculate the area of a trapezoid.
height = int(input())
base1 = int(input())
base2 = int(input())
area =(base1 + base2)* height /2
print (area)


#Write a Python program to calculate the area of regular polygon.
n = int(input())
s = int(input())
degree = 360 / (2*n)
radian = degree /180 * math.pi
a = s/2 * (1/math.tan(radian))
p = n*s
area = p*a/2

print(area)



#Write a Python program to calculate the area of a parallelogram.

a = float (input())
b = float (input())

print (a*b)