def insertion_sort(arr):
    """
    \n Description: Function to sort the array using insertion sort algorithm \n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n^2) \n
    """
    n = len(arr)

    for i in range(1, n):
        insert_index = i
        current_ele = arr[i]

        for j in range(i-1, -1, -1):
            if arr[j] > current_ele:
                arr[j+1] = arr[j]
                insert_index = j
        arr[insert_index] = current_ele
    return arr

if __name__ == "__main__":
    print(insertion_sort([5,3,7,9,1,2,3,1,3,0,5,2,9,1]))