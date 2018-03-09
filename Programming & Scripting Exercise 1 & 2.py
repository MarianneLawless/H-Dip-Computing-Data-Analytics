
# Week 1 Exercise

# Fibonacci (https://en.wikipedia.org/wiki/Fibonacci_number)

def fib(n):
  """This function returns the nth Fibonacci number."""
 
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
  
# Week 2 Exercise
# Fibonacci numbers using people's names.

name = "Lawless
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Python is a programming language. The Python interpreter has a number of functions built in, one of these basic functions is know as ord(), which represents a type of built in formula into the program, per say, when run giving us a desired output. We know that the computer only understands bits and bytes. The characters we type in are encoded as bits, the Python Interpreter, converts these characters to ASCII value, we interpret these bits as some numbers that represent those characters we fed. So the basic function, ord(), when run e.g ord(L) as in the week task,  the interpreter returns the ASCII value of a character L within the this function as 76.

As in the example below...
The first letter L is number 76 ord(first)
The last letter s is number 115 ord(last)
name = "Lawless"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno
