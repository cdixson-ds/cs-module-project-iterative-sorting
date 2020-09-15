def partition(arr):
    pivot = arr[0]
    left = []
    right = []

    #partition the elements around the pivot
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    #we have elements partitioned in the left, pivot and right arrays
    return left, pivot, right  #returns partitioned elements along with the pivot

def quicksort(arr):
    #base case: if the len of the array is <= 1
    if len(arr) <= 1:
        return arr

        #otherwise, we need to call our partition funx to break the input array
        #into smaller chunks
        left, pivot, right = partition(arr)

        qleft = quicksort(left)
        qright = quicksort(right)

        return qleft + pivot + qright