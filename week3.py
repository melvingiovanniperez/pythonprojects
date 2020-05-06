import math

def circle_area(radius):
   return  math.pi*radius**2
    
def triangle_area(base, height):
    return base*height*0.5

def tripler(s):
    return s*3

def fruitval(fruit):
    if fruit == 'pear':
        return 7
    elif fruit == 'banana':
        return 4
    else:
        return 3

def one_of(n, v1, v2):
    if n%2 == 0:
        return v2
    else:
        return v1

def hide_string(s, char):
    return char*len(s)

def five():
    for n in range (1000, 1050, 10):
        print(n)

def odd_part(n):
    while n%2 == 0:
       n = n/2
    return int(n)

import random

def countrand(limit):
    sum = 0
    counter = 0
    while sum < limit:
        sum = sum + random.random()
        counter = counter + 1
    return counter

