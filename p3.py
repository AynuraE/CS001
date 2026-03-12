#Fibonacci sequence

def func_fib(n): #parameter is Fibonacci number limit
    count = 0
    a, b = 1, 1
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1

func_fib(10)

#Define a function that takes a limit as a parameter and prints the numbers in the Fibonacci sequence until the sum of those
# numbers is greater than or equal to limit

def fib_limit(limit):
    a = 1
    b = 1
    sum = 0
    while sum < limit:
        print(a)
        sum += a
        c = a + b
        a = b
        b = c

fib_limit(100)

#Define a function that takes a limit as a parameter and returns the sum of Fibonacci numbers
# is greater than or equal to limit

def fib_limit(limit):
    a = 1
    b = 1
    sum = 0
    while sum < limit:
        sum += a
        c = a + b
        a = b
        b = c
    return sum

print(fib_limit(100))
