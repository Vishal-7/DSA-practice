def quicksort(arr, low=0, high=None):
    """
    \n Description: Function to sort the array using the concept of quicksort \n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n^2) \n
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_element = partition(arr, low, high)
        quicksort(arr, low, pivot_element - 1)
        quicksort(arr, pivot_element + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1

if __name__ == "__main__":
    my_array = [64, 34, 25, 12, 22, 11, 90, 5]
    quicksort(my_array)
    print(f"Sorted array: {my_array}")