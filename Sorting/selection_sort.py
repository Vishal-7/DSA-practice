def selection_sort(arr) -> list:
    """
    \n Description: Function used to sort the elements using selection sort algorithm \n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n^2) \n
    """
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    print(selection_sort([5,3,7,9,1,2,3,1,3,0,5,2,9,1]))