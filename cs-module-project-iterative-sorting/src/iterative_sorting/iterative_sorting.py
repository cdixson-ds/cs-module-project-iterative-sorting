# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  #loop that moves the boundary
        smallest_index = i            #keep track of smallest element

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)): #i+1 cuts off one single redundant iteration
            if arr[smallest_index] > arr[j]:
                smallest_index = j
      

        # TO-DO: swap
        # Your code here

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]   #swap

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # keep a flag that tracks whether any swaps occured

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  #swap

    return arr


# Lecture example

# def bubble_sort(arr):
#     # Your code here
#     # keep a flag that tracks whether any swaps occured
#     swaps_occured = True
#     while swaps_occured:
#         swaps_occured = False
        
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i] > arr[i+1]
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swaps_occured = True

#     return arr


"""

STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


#Notes from lecture

def counting_sort(arr, maximum=None):
    # Your code here
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]
    #loop through array
    for value in arr:
        #for each distinct arr value, increment by 1
        buckets[value] += 1

    #at this point our buckets array has all of the counts of every distinct
    #val in our input array

    output = []

    for index, count in enumerate(buckets):     #each step makes a mini list
        output.extend(index for i in range(count))  #extend appends list? revisit

    return output
    
