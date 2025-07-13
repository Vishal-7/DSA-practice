from typing import List

def consec_ones_zeros(arr: List[int]) -> int:
    cnt = 0
    maxi = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt = 0
        maxi = max(maxi, cnt)
    return maxi


if __name__ == "__main__":
    arr = [1, 0, 1, 1, 0, 1]
    print(consec_ones_zeros(arr=arr))