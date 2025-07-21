from typing import List

def longest_subarray_sum(arr: List[int], n: int, k: int) -> int:
    """
    \n Description: Funcion to find the length of the longest subarray with given sum \n
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

if __name__ == "__main__":
    arr, k = [10, 5, 2, 7, 1, 9], 15
    print(longest_subarray_sum(arr=arr, n=len(arr), k=k))