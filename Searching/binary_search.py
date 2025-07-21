from typing import List

def bin_search(arr: List[int], low: int, high: int, target: int) -> int:
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return bin_search(arr, low, mid-1, target)
        else:
            return bin_search(arr, mid+1, high, target)
    else:
        return -1

if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40 ]
    x = 100
    print(bin_search(arr, 0, len(arr)-1, x))