# -*- coding: utf-8 -*-
import time
"""
Created on Fri Sep  6 13:40:13 2019
Lab 1 - Recursion
This program will be divided into two part.
Part one, looks for anagrams of a word from a list and will print them out 
inside another list. It turns each word into a list and then checks of it 
has the same lenght and letter within.

Part Two: takes a word and generates all the possible permutations of the 
word, 



@author: Kevin Ramirez
"""
def Is_Anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()
    
    return (list_str1 == list_str2)

#read from file and make into set
my_set = set(line.strip() for line in open('ReadtThisPyt.txt'))

#set to list with sort in alphabetical order
List_Txt = list(my_set)
List_Txt.sort()

print("Enter a word or empty string to finish:")
#User input that will be use to check for anagrams
User_Input = input() 
#turn the users input into a list, then sorts the list alphabetically 
List_Input = list(User_Input)
List_Input.sort()

#THIS ONE IS RIDICULOUS, if i give it all the 466,000 it crashes my PC
def Done_anagram(List_Input, List_Txt):
    if len(List_Txt) == 0:
        return ""
    else:
        S = Done_anagram(List_Input, List_Txt[1:])
        if Is_Anagram(List_Input, List_Txt[0]):
            return List_Txt[0] + "\n" + S
        else:
            return S

Start_Time = time.time()
print (Done_anagram(List_Input, List_Txt))
End_Time = time.time()
print(End_Time - Start_Time)

#Second part 
def Anagram_permutation(User_Input, sample_word): 
    # Disclamer this one is the example from the book... 
    # I did try my own tho, its below this one
    if len(User_Input) == 0:
        # Base case: All letters used
        print(sample_word)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(User_Input)):
            # The letter at index i will be scrambled
            scramble_letter = User_Input[i]
            
            # Remove letter to scramble from remaining letters list
            remaining_letters = User_Input[:i] + User_Input[i+1:]
            
            # Scramble letter
            Anagram_permutation(remaining_letters, sample_word + scramble_letter)

Start_Time = time.time()
Anagram_permutation(User_Input, '')
End_Time = time.time()
print(End_Time - Start_Time)




# Second part (not being used since it doesnt work right)
def Anagram_Permutations(A, B = ''):
    #The expression is tested, and if the result comes up false, an exception is raised.
    assert len(A) >= 0
    assert len(A) == len(set(A))
    # Base Case, if the word list is 0, return empty
    if len(A) == 0:
        return [B]
    else:
        #holder keeps the permutations in a list 
        holder = []        
        for i in range(len(A)):
            holder.extend(Anagram_Permutations(A[0:i] + A[i+1:], B + A[i]))

        return holder











