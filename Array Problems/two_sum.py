from typing import List

def two_sum(arr1: List[int], target: int, n: int) -> tuple:
    """
    \n Description: Function to find the pair matching the target \n
    \n Input: input array; target number; size of array; \n
    \n Output: tuple containing the indices of the pair \n
    \n Time Complexity: O(n^2) \n
    """
    for i in range(n):
        for j in range(i, n):
            if arr1[i] + arr1[j] == target:
                return (i, j)
    return (-1, -1)

def two_pointer_twosum(arr1: List[int], target: int, n: int) -> tuple:
    """
    \n Description: Two sum implememntation using two pointer concept \n
    \n Input: input array; target number; size of array; \n
    \n Output: tuple containing the indices of the pair \n
    \n Time Complexity: O(n) + O(n logn) \n
    """
    arr1.sort()

    left, right = 0, n-1
    while left < right:
        tot = arr1[left] + arr1[right]
        # print(f"Left: {arr1[left]} || Right:{arr1[right]} || Total: {tot}")
        if tot == target:
            return (arr1[left], arr1[right])
        elif tot < target:
            left += 1
        else:
            right -= 1
    return (-1, -1) 

def twosum_hashmap(arr1: List[int], target: int, n: int) -> tuple:
    """
    \n Description: Function to find the pair whose summation equals the target \n
    \n Input: Input array; target value; length of array \n
    \n Output: Tuple with the indices of the pair of numbers \n
    \n Time Complexity: O(n) \n

    """
    hash = {}

    for i in range(n):
        bal = target - arr1[i]
        if bal in hash:
            print(hash)
            return (i, hash.get(bal))
        hash[arr1[i]] = i
    print(hash)
    return (-1, -1)

if  __name__ == "__main__":
    # print(two_pointer_twosum([1, 6, 2, 10, 3], 7, 5))
    # print(two_sum(arr1=[2,6,5,8,11], target=14, n=5))
    print(twosum_hashmap([2,6,5,8,11], 14, 5))