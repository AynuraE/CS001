#Author: Aynura Erejepbaeva
#Date: 10/13/2025
#Purpose: Demo building strings
s = ""
s = s + "a"
s = s + "b"
s = s + "c"
print(s)

#Reversing a string
def reverse_s(gs):
    rs = ""
    for ch in gs: #goes over each character in the given glist
        rs = ch + rs
    return rs
res = reverse_s("abcd")
print(res)

#Nested loops
i = 1
while i <= 5:
    j = 1
    while j < 5:
        print(i, j)
        j = j + 1
    i = i + 1

#Define a function that takes a list of positive integers, glist, as a parameter and prints all pairs of numbers where one is the square of the other.
# Example: [4, 25, 7, 2, 16, 5, 1], your function should print the following pairs in some order
#4 2
#25 5
#4 16
#1 1
#2 4
#5 25
#16 4

def func1(glist):
    i = 0
    while i < len(glist): #i is index of first number
        j = 0
        while j < len(glist): #j is index of second number
            if glist[i] == glist[j] * glist[j] or glist[j] == glist[i] * glist[i]:
                print(glist[i], glist[j])
            j = j + 1

        i = i + 1
func1([4, 25, 7, 1, 16, 2, 5])
print("----")

#Variation1: A number cannot be paired with itself
def func2(glist):
    i = 0
    while i < len(glist):  # i is index of first number
        j = 0
        while j < len(glist):  # j is index of second number
            if i != j:
             if glist[i] == glist[j] * glist[j] or glist[j] == glist[i] * glist[i]:
                print(glist[i], glist[j])
            j = j + 1

        i = i + 1

func2([4, 25, 7, 1, 16, 2, 5])
print("----")

#Variation2: Each number should be paired with the other only once
def func1(glist):
    i = 0
    while i < len(glist):  # i is index of first number
        j = i
        while j < len(glist):  # j is index of second number
            if glist[i] == glist[j] * glist[j] or glist[j] == glist[i] * glist[i]:
                print(glist[i], glist[j])
            j = j + 1

        i = i + 1

func1([4, 25, 7, 1, 16, 2, 5])
print("----")

#Applying an operation to all elements in the list
#

#Variation 1: Define a function that takes a list of positive integers as a parameter and returns True if all the elements in the list are prime numbers. Otherwise, it returns False.

#Variation 2: Define a function that takes a list of positive integers

#Nested loops example 3: Define a function that takes a list of strings, glist, as a parameter and prints all pairs of strings in glist that have equal
# number of a's. Mustn't pair a string with itself and a pair should be printed only once. Assume the string in glist are unique. Find pairs of strings.

#given two strings equal number of a's. Count the number as a's in a string.
def count_a(gs):
    count = 0
    for ch in gs: #goes over the characters in gs
        if ch == "a":
            count = count + 1
    return count

#given two strings equal to number of a's
def equal_a(gs1, gs2):
    c1 = count_a(gs1)
    c2 = count_a(gs2)
    return c1 == c2

#find pairs of strings
def find_pairs(glist):
    for i in range(0, len(glist)):
        s1 = glist[i] #s1 is the first string in the pair
        for j in range(i+1, len(glist)): #s2 is the second string in the pair
            s2 = glist[j]

            check = equal_a(s1, s2)
            if check == True:
                print(s1, s2)

find_pairs(["mango", "banana", "Dartmouth", "aa", "exam"])