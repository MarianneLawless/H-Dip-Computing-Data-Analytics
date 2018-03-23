
# Marianne Lawless
# Exercise 6 - Functions
# Write a Python script containing a function , and call the function factorial()
# Adapted from nbviewer.jupyter.org/github/ianmcloughlin/python-fundame

def factorial(f):
    ans = 1 # number I am looking for 
    for i in range(1, f + 1): # Every time python goes around the loop, it adds 1
        ans = ans * i # my ans multiplied the new value for i 
    return ans

print(factorial(5))
print(factorial(7))
print(factorial(10))
The factorial of 5 is 120
The factorial of 7 is 5040
The factorial of 10 is 3628800
