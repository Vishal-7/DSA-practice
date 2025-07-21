from typing import List

def num_occurance(arr: List) -> int:
    """
    \n Description: Function to find the number occuring only once in the given list \n
    \n Input: unsorted array \n
    \n Output: integer occuring only once \n
    \n Time Complexity: O(n) \n
    """
    temp = {}

    for num in arr:
        temp[num] = temp.get(num, 0) + 1
    
    for i in temp:
        if temp[i] == 1:
            return i
    else:
        return -1
    
if __name__ == "__main__":
    arr = [4,1,2,1,2]
    print(num_occurance(arr=arr))