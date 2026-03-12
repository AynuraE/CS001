#Purpose: Quiz 02 Review

#SA06 need to be on quiz
# going over:
    # list of lists
    # helper functions
    # construction
    #iterating

    # loops, nested loops
    # for loops vs while loops
    # list slice notation
    #temporary/aux variables

#i-list canonically makes a list of integers
#lol list or general list
#s-list list of strings


#BASIC LOOPS______________________
#if given non-empty list of integers---called i-list---make a new list consisting of even integers in i-list
    #can score points KEYWORDS: new list, even integers, i-list
    #things I know: new[] or =list()...these make a new list
        #value: if val%2==0:
    # i=0
    # while i< len(new)

    #SOLUTION:
        #new_list=[]
            # always need a counter b/c you need to index the list
        #i=0
            # know you need to update, so INDENT and i=i+1
         #while i < len(i-list):
            # INDEX starts at 0, so do only LESS THAN and not LESS THAN AND EQUAL TO
            #if i-list[i]%2==0:
                #asking for value not index in this example
                #new_list.append(i-list[i])
            #i=i+1
        #print(new_list)

# note: can only use return in a function
    #def evens(i-list):
        #new_list=[]
        #i=0
        #while i < len(i-list):
            #if i-list[i]%2==0:
                #new_list.append(i-list[i])
            #i=i+1
        #return new_list
    #alist=[1,2,3,4]
    #print(evens(alist))

# doing this example with a for-loop
    #i-list=[1,2,3,4]
    #i=0
    #while i<len(i-list):
        #print(i-list[i])
        #i=i+1

    #for x in list: #x is the element in i-list
        #print(x)   #already have value of x in python


    #print(i-list[i])
    #print(i)

#one of the things you can use fir list operations: RANGE PARAMETER--generator function
    #for i in range(0,len(i-list),1):
        #print(i-list[i])
        #print(i)

#SLICED NOTATION_______________________
    #range(1,len(alist)-2,3)

    #alist[1:len(alist),1]


    #alist=[1,2,3,4,5,6,7,8]
    #blist=[alist[1,len(alist)-2,3]]
    #for x in b list:
        #print(x)
#doing a while-loop variation
    #alist...
    #blist=[]
    #i=1
    #while i<len(alist)-2:
        #blist.append(alist[i])
        #i=i+3 OR i+=3 NOT i=+3 (which means i=-3)


#NESTED LOOPS___________
#use evens function that's already written

#THIS EX IS NOT A NESTED LOOP, THIS IS USING A HELPER FUNCTION EX
    #def evens(i_list)
    #def sum_evens(i_list):
        #evens_list=evens(i_list)
        #sum=0  #in case there are no even numbers
        #i=0
        #while i<len(evens_list):
            #sum+=evens_list[i]
            #i=i+1
        #return sum

#NESTED LOOP EX
#list of strings, want a new list that consists of the strings of the given list that are palindromes
#write a function called find_palindromes
    #words=["cat","dad","mom"]
    #def is_pds(word):  #helper function
        #i=0
        #while i<len(word):
            #if word[i]!=word[len(word)-i-1]:
                #return False
            #i=i+1
        #return True
    #def find_pds(words):   #main function
        #pds=[] #need a new list
        #for w in words:    #iterate through words
            #if is_pds(w):  #is it a palindrome?
                #pds.append(w)  #add to pds[]
        #return pds


    #using while loop instead of for loop
#def find_pds(words):
    #pds=[]
    #i=0
    #while i<len(words):
        #w=words[i]
        #if is_pds(w):
        #    pds.append(w)
        #i=i+1
    #return pds

#find_pds(["cat","mom","dad"])   #if you don't make the list beforehand---THIS WILL DO NOTHING WITHOUT print func
#print(find_pds(["cat","mom","dad"])

#ENUMORATE FUNCTION???