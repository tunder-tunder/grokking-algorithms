# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:59:00 2022

@author: tunder

Grokking Algorithms by Aditya Bhargava
Done in order to refresh my memory and store them all in one place 
(･ω<)☆
"""
#binary search ch1
def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
    return None 

# find the min in the array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# selection Sort ch2
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

my_list = [10, 2, 4, 1, 5, 20]
print(f"Testing array {my_list}")
print("binary search: ", binary_search(my_list, 1))
print("selection sort (sort from min to max): ", selection_sort(my_list))

