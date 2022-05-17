# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:18:50 2022 9:19 pm - 9:38 pm

@author: 2063176
"""

#linear search
"""
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].

------------------
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
----------
"""
# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def search(arr, n, x):
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1
#driver code
arr = [10,20,30,40,50]
x=40
n = len(arr)
 
#function call
result = search(arr,n,x)
if(result == -1):
    print("Element x is not present in arr[]")
else:
    print("Element x is present at index "+ str(result))
    















