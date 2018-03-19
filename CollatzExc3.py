# Marianne Lawless
# Programming & Scripting Exercise 3
# Adapted from https://en.wikipedia.org/wiki/Collatz_conjecture

n = 1 # value of n 

while n <= 1: # while n is less than or equal to 1
    if (n % 2 == 0): # if n is an even number, do the following 
        n = n / 2 # divide n by 2 
    else: # otherwise
        n = n*3 + 1 # mutiply n by 3 and add 1
        print(n)

n = n + 1

print ("The final value of n is:" , n )  

    