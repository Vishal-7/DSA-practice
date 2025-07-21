from typing import List

def print_max_element(arr: List) -> int:
    """
    \n Description: Function to find the element occuring more than half of the length of input \n
    \n Input: unsorted list \n
    \n Output: maximum occuring element \n
    \n Time Complexity: O(n+m) \n
    """
    n, max_val = len(arr), 0


    hash_map = [0] * ((max(arr))+1)

    for i in arr:
        hash_map[i] += 1
    
    for j in range(len(hash_map)):
        if hash_map[j] > n//2:
            return j
    return -1

if __name__ == "__main__":
    print(print_max_element([4,4,2,4,3,4,4,3,2,4]))
