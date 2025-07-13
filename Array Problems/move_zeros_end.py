from typing import List

def move_zeros_end(arr: List[int]) -> List[int]:
    """
    \n  Description: Function to move all zeeros to end if list and non zero to the front \n
    \n Input: array with zeros and non zero numbers \n
    \n Output: array with all the zeros at the end of the list \n
    \n Time Complexity: O(n)
    """
    n = len(arr)

    i = 0
    j = i + 1

    while i < len(arr) and j < len(arr):
        if arr[i] == 0 and arr[j] == 0:
            j += 1

        elif arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1

        elif (arr[i] != 0 and arr[j] == 0) or (arr[i] != 0 and arr[j] != 0):
            i += 1
            j += 1
    return arr

if __name__ == "__main__":
    arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
    print(move_zeros_end(arr=arr))