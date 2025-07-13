from typing import List

def left_rotate(arr: List[int]) -> List:
    """
    """
    temp = [0] * len(arr)

    for j in range(1, len(arr)):
        temp[j-1] = arr[j]
    
    temp[len(arr)-1] = arr[0]

    return temp

def left_rotate_optimised(arr: List[int]) -> List:
    temp = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]
    
    arr[-1] = temp
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(left_rotate(arr))

    print(left_rotate_optimised(arr))
    print([1,2,3,4,5][:-3])