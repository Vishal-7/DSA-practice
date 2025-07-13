from typing import List

def missing_ele(arr: List[int], N: int) -> int|List:
    hash_table = [0] * (N+1)
    for i in range(N-1):
        hash_table[arr[i]] += 1
    
    for i in range(1, len(hash_table)):
        if hash_table[i] == 0:
            return i

if __name__ == "__main__":
    arr = [1,2,4,5]
    print(missing_ele(arr=arr, N=5))