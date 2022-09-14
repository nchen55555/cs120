from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""
def print_arr(arr): 
    for i in range(len(arr)): 
        print("(", arr[i][0], ", ", arr[i][1], ")", end = ", ")

def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, b, arr): 
    k = math.ceil (math.log2(univsize)/math.log2(b))
    n = len(arr)
    temp_array = []
    for i in range(n): 
        v_sub = BC(arr[i][0], b, k)
        temp_array.append([arr[i][0],[arr[i][1], v_sub]])
    for j in range(k): 
        for i in range(n): 
            temp_array[i][0] = temp_array[i][1][1][j]
        temp_array = countSort(b, temp_array)
    for i in range(n): 
        for j in range(k): #can we consolidate here
            if j == 0: 
                arr[i][0] = temp_array[i][1][1][j] * pow(b,j)
            else: 
                arr[i][0] += temp_array[i][1][1][j] * pow(b,j)
        arr[i][1] = temp_array[i][1][0]
    return arr

def tests(): 
    for univSize in range(0,1):
        for nSize in range(1,17):
            #print("U ", univSize, " N ", nSize)
            u = pow(2,univSize)
            n = pow(2,nSize)
            random_array = []
            for i in range(n): 
                random_array.append([random.randint(0, u-1), 0])
            #print("Running Merge Sort: ", end = "")
            #start = time.time()
            #mergeSort(random_array)
            #end = time.time()
            #print((end-start) *1000, "ms", end = "\n")
            #print("Running Count Sort: ", end = "")
            #start = time.time()
            #countSort(u, random_array)
            #end = time.time()
            #print((end-start)*1000, "ms", end = "\n")
            #print("Running Radix Sort: ", end = "")
            start = time.time()
            radixSort(u, n, random_array)
            end = time.time()
            print((end-start)*1000, "ms", end = "\n")

if __name__ == "__main__":
    tests()
