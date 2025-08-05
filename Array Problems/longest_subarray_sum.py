from typing import List

def longest_subarray_sum(arr: List[int], n: int, k: int) -> int:
    """
    \n Description: Function to find the length of the longest subarray with given sum \n
    \n Input: unsorted array, length of array, target sum \n
    \n Output: Length of the longest subarray with given sum \n
    \n Time Complexity: O(2*n) = O(n) \n
    """
    left, right = 0, 0
    Sum = arr[0]
    maxLen = 0

    while right < n:
        while left <= right and Sum > k:
            Sum -= arr[left]
            left += 1

        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
        if right < n:
            Sum += arr[right]
    return maxLen

def longest_subarray_hashing(arr: List[int], n: int, k: int) -> int:
    """
    \n Description: Function to find the length of the longest subarray with givrn array using hashing concept \n
    \n Input: unsorted array, length og array, target sum \n
    \n Output: Length of the longest subarray with given target sum \n
    \n Time Complexity: O(n logn) \n
    """
    preSumMap = {}
    Sum = 0
    maxLen = 0

    for i in range(n):
        Sum += arr[i]

        if Sum == k:
            maxLen = max(maxLen, i+1)
        
        rem = Sum - k

        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        
        if Sum not in preSumMap:
            preSumMap[Sum] = i
    
    return maxLen

if __name__ == "__main__":
    arr, k = [-1, 1, 1], 1
    # arr, k = [-2,1,-3,4,-1,2,1,-5,4], 6
    print(longest_subarray_sum(arr=arr, n=len(arr), k=k))
    print(longest_subarray_hashing(arr=arr, n=len(arr), k=k))