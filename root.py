import math

def find_root(number):
    guess = 1
    for i in range(1, 11):
       guess = ((number/guess)+guess)/2
       print('After iteration',i,'my guess is',guess)


def main():
    number = float(input('Write a number'))
    find_root(number)
    answer= math.sqrt(number)
    print('The answer is',answer)

main() 
   
