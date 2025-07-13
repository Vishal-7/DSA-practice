def array_sorted(arr: list) -> bool:
    """
    \n Description: Function to find if the array is sorted or not \n
    \n Input: Sample array \n
    \n Output: array sorting status; Boolean (True // False) \n
    \n Time Complexity: 
    """
    if len(arr) < 2:
        return True
    
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i+1]:
            return False
    return True

if __name__ == "__main__":
    arr = [5, 4, 6, 7, 8]
    print(array_sorted(arr))