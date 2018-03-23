# Marianne Lawless
# Exercise 6 - Functions
# Write a Python script containing a function , and call the function factorial()

def factorial(f): # Function defined as factorial (f)
    n = 1 
    while f >= 1: # While f is greater than / equl to 1
        n = n * f # My starting number n multiplied by the number f ..factorial number 
        f = f - 1 # loops from f to 0, subtracting 1 on every loop
    return n

print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))

The factorial of 5 is 120
The factorial of 7 is 5040
The factorial of 10 is 3628800
