#return statements recap

def func1(n):
    m = n*n #25
    return m

def func2(m):
    return m+10

def func3(m):
    print(m)
    if m > 100:
        return m
    return m + 100

v1 = func1(5)
print(v1 + func2(10))
v2 = func1(func2(0))
print(v2)

print(func3(100))

#break out of a while loop
i = 0
while i < 10:
    if i == 3 and i % 2 == 0:
        break #break is like a return but it doesn't return anything
    i = i + 1

print(i)

#optional parameters
def func1(m=5, n=10):
    print(m, n)

func1(n=25, m=100) #my function gets the values from here, which are replaced from the first variables

angles = [90, 45, 35]
print(angles)
print(angles[1])
print(type(angles)) #type of the list
print(len(angles)) #length of the list
print(angles[2]) #last item in the list
print(angles[len(angles)-1])

temperature = [-5, -9, -10, -15, -19]
print(temperature[1:4]) #return the values between 1 and 4, which are -9, -10, -15
print(temperature[1:len(temperature)])
print(temperature[2:])

print(temperature[ ::-1 ]) #it's assuming that we need to go backwards and

i = 0
while i < len(temperature):
    print(temperature[i])
    i = i + 1

#To print out the letter C
name = "Michael Casey"
i = 0
while i < len(name):
    if i < len(name)-1 and name[i] == " ":
        print(name[i+1])
    i = i + 1

def func1(glist):
    glist[0] = 101
    print(glist)

alist = [45, 23]
func1(alist)
print(alist)

#Define a function that takes a non-empty string as a parameter and returns the length of the longest substring that is a palindrome.

#Function to check if a given string is a palindrome

def is_palindrome(gs):
    i = 0
    j = len(gs) - 1
    while i < j:
        if gs[i] != gs[j]:
            return False
        i = i + 1
        j = j - 1

    return True

def find_substrings(gs):
    max_l = 0
    l = 2
    while l <= len(gs):
        p = 0
        while p <= len(gs) - l:
            ss = gs[p:p+l]
            if is_palindrome(ss) and len(ss) > max_l:
                max_l = len(ss)
                print("longest so far", ss)
            p = p + 1
        l = l + 1
    return max_l

find_substrings("abcdaadefg")
    