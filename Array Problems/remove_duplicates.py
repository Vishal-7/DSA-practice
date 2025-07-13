from typing import List

def remove_duplicates(arr: List[int]) -> list:
    """
    \n Description: Function to remove the duplicates from the list \n
    \n Input: array with duplicate values \n
    \n Output: array without the duplicate values \n
    \n Time Complexity: O(n)
    """
    temp_storage = []

    for i in arr:
        if i not in temp_storage:
            temp_storage.append(i)
    return temp_storage

def remove_duplicates_2pointer(arr: List[int]) -> int:
    """
    \n Description: Function to remove the duplicates from array using two pointer concept \n
    \n Input: array with duplicate values \n
    \n Output: Int value till which non duplicate values are present in the list \n
    \n Time Complexity: O(n)
    """
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3]
    print(remove_duplicates(arr))

    k = remove_duplicates_2pointer(arr)
    for i in range(k):
        print(arr[i], end=" ")