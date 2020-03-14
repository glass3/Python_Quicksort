import time
import numpy as np

def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    j = low
    while(j < high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j+=1
    temp1 = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp1
    return i + 1
def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

with open('data.txt') as f:
    lines = f.read().splitlines()

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

a = np.array(lines)

t1_start = time.perf_counter()

#Uncomment which version to test

#Quicksort with python list
#quicksort(lines,0,len(a)-1)

#Quicksort with Numpy array
#quicksort(a,0,len(a)-1)

#Numpy's built in quicksort
#np.sort(a)

t1_stop = time.perf_counter()
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)