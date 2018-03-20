# Marianne Lawless
# Problem 5 Project Euler
 
i = 1 # starting from 1
n = 1 # smallest positive number I am looking for
l = 2520

while i < 21:
  for i in range (11,21,2):
    if n % i == 0: #f must be an even number
       i = i + 1 + l  #add 1 to the number
else: # otherwise
    n = n + 1 + l #add a number to the number I am looking for 
    i = 1
    l = 2520

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is n:", n) 