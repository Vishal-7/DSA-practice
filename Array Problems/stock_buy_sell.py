from typing import List

def stock_buy_sell(arr: List[int]) -> int:
    """
    \n Description: Function to find the best profit price after buying and selling a share \n
    \n Input: Array filled with stock values \n
    \n Output: The best profit price \n
    \n Time Complexity: 
    """
    n = len(arr)
    sum_mx = 0
    for i in range(n-1):
        for j in range(i+1, n):
            # print(arr[j] - arr[i])
            sum_mx = max(sum_mx, arr[j]-arr[i])
    return sum_mx

def stock_buy_sell_optimised(arr: List[int]) -> int:
    minSoFar = arr[0]
    res = 0

    for i in range(1, len(arr)):
        minSoFar = min(minSoFar, arr[i])

        res = max(res, arr[i] - minSoFar)
    return res

if __name__ == "__main__":
    arr = [7, 10, 1, 3, 6, 9, 2]
    # print(stock_buy_sell(arr=arr))

    print(stock_buy_sell_optimised(arr=arr))