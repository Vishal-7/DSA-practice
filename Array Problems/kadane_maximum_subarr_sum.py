from typing import List
import sys

def kadane_maxsubarr(arr: List[int]) -> int:
    n = len(arr)
    maxi = -sys.maxsize - 1
    
    for i in range(n):
        for j in range(1, n):
            sum_temp = 0
            for k in range(i, j+1):
                sum_temp += arr[k]
            maxi = max(maxi, sum_temp)
    return maxi

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane_maxsubarr(arr=arr))