from typing import List

def linear_search(arr: List[int], target: int):
    """
    \n Description: Function to find the position of the target element in the input list \n
    \n Input: array; target; \n
    \n Output: int -> if number is found, str -> if number not found \n
    \n Time Complexity: O(n) \n
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Number not present in the input list"

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    target = 5
    print(linear_search(arr=arr, target=target))