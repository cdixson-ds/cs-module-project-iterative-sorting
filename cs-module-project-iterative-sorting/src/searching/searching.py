def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) -1
    mid = 0
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid

    return -1  # not found


    #######################################3

    def binary_search(arr, target):
        #keep track of left and right edges as well as midpoint
        left = 0
        right = len(arr)                 
        midpoint = len(arr) // 2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            #toss out left side of the array and midpoint
            left = midpoint + 1

        else: 
            right = midpoint - 1 #don't include midpoint element


    return -1  # not found
