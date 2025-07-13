def mergeSort(arr):
    """
    \n Description: Function to sort the array using the merge sort algorithm\n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n log n) \n
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 # split the array into half

    left_half = arr[:mid]
    right_half = arr[mid:]

    sortedLeft = mergeSort(left_half) # recurssion to split the array again
    sortedRight = mergeSort(right_half)

    return merge(sortedLeft, sortedRight) # merge the split array

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)