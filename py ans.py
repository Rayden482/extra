# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:23:45 2020

@author: Parag kapoor
"""
def partition(target_list,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = target_list[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   target_list[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            target_list[i],target_list[j] = target_list[j],target_list[i] 
  
    target_list[i+1],target_list[high] = target_list[high],target_list[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(target_list,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(target_list,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(target_list, low, pi-1) 
        quickSort(target_list, pi+1, high) 

def largest_two(target_list):
    arr=list(target_list)
    n=len(arr)
    quickSort(arr, 0, n-1)
    print("The largest and second largest elements in the list {} are {} and {}".format(target_list,arr[-1],arr[-2]))
    
