def bubble_sort(arr) -> list:
    """
    \n Description: Function to implement the bubble sort algorithm \n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n^2) \n
    """
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([5,3,7,9,1,2,3,1,3,0,5,2,9,1]))