# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:03:49 2019
Lab#2 

@author: Kevin Ramirez
Date: September 21, 2019
Professor: Olac Fuentes

Purpose: Develope multiple implementations of quick sort by
using normal quick sort, a modified version of quick sort, 
a quick sort that uses a while loop, and a quick sort that 
uses stacks instead of recursions or while loops, and create
a normal bubble sort, and these are have to return the smallest 
Kth element.

"""

#PART #1
# bubble sort:
# pretty simple, the 
    
def bubble_call(lst,k=0):
    if len(lst)== 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    
    Bubble_Sort(lst)
    return lst[k]


def Bubble_Sort (lst):
    lst_size = len(lst)
    for count in range(lst_size):
        for b in range((lst_size - 1) - count):
            if(lst[b]>=lst[b+1]): #swaps elements
               lst[b], lst[b+1] = lst[b+1], lst[b]     
    #print(lst)
    return lst 

# NORMAL QUICK SORT 

def Quick_parti(lst, left_start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    pivot = left_start
    for i in range(left_start, end):
        if lst[i] < lst[end]:
            lst[i], lst[pivot] = lst[pivot], lst[i]
            pivot = pivot + 1
    lst[pivot], lst[end] = lst[end], lst[pivot]
    #print(lst)
    return pivot

def quick_sort(lst, left_start, end):
    if left_start >= end:
        return lst
    #pivot = left_start #chage this Not needed
    #print('this is you pivot', lst[pivot])
    new_pivot = Quick_parti(lst, left_start, end, pivot = left_start)
    quick_sort(lst, left_start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)
    #print(lst)

def Q_sort_call(lst, k=0):
    if len(lst) == 0:
        return None
    elif len(lst) ==1:
        return lst[0]
    
    quick_sort(lst, 0, len(lst) - 1)
    return lst[k]

#MODIFIED VERSION OF QUICK SORT

def Partion_quick_sort(lst, start, end):
    check = start - 1
    
    pivot = lst[end]
    
    for j in range(start, end):
        if lst[j] <= pivot:
            check = check + 1
    
            lst[check], lst[j] = lst[j], lst[check]
            
    lst[check + 1], lst[end] = lst[end], lst[check + 1]

    return check + 1

def Mod_Quick(lst, start, end, k):
    piv = Partion_quick_sort(lst, start, end)
    if k < piv:
        #print(lst)
        return Mod_Quick(lst, start, piv - 1, k)
    elif k > piv:
        #print(lst)
        return Mod_Quick(lst, piv + 1, end, k)
    else:
        #print(lst)
        return lst[piv]
   
    
def Mod_Quick_Call(lst, k):
    if len(lst)==0:
        return None
    elif len(lst)==1:
        return lst[0]
    start = 0
    end = len(lst) - 1
    return Mod_Quick(lst, start, end, k)

#THIS IT THE WHILE LOOP QUICKSORT
# All of the print statements are just for debugging the method   
def Quicksort_while(lst, start, end, mid, k=0):
    New_pivo = Partion_quick_sort(lst, start, end)
    #print("This is your mid:", mid)
    #print("This is the new Piv:", New_pivo)
    while New_pivo != mid:
        if(mid < New_pivo):
            New_pivo = Partion_quick_sort(lst, start, New_pivo -1)
            #print("this is the second Piv:", New_pivo)
        elif(mid > New_pivo):
            New_pivo = Partion_quick_sort(lst, New_pivo + 1, end)
            #print("this is the third Piv:", New_pivo)
    return lst[k]


def Quick_W_call(lst, k):
    mid = (len(lst)//2)-1
    start = 0
    end = len(lst) - 1
    return Quicksort_while(lst, start, end, mid, k)

#QUICK SORT WITH STACKS
    #i Was not able to finish the quick sort with stacks

FINAL_LIST = [1,23,34,4,-5]

print("this is bubble: ", bubble_call(FINAL_LIST, 0))
print(FINAL_LIST)
print("This is the normal quick sort: " , Q_sort_call(FINAL_LIST, 0))
print(FINAL_LIST)
print("This is the modified quick sort", Mod_Quick_Call(FINAL_LIST, 0))
print(FINAL_LIST)
print("This is the quick sort while", Quick_W_call(FINAL_LIST, 0))
print(FINAL_LIST)



