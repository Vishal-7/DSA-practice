from typing import List

def union_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    unique_dict = {}

    for num1 in arr1:
        unique_dict[num1] = unique_dict.get(num1, 0) + 1
    
    for num2 in arr2:
        unique_dict[num2] = unique_dict.get(num2, 0) + 1
    
    return list(unique_dict.keys())

def union_arrays_sets(arr1: List[int], arr2: List[int]) -> List[int]:
    return list(set(arr1) | set(arr2))

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    # print(union_arrays(arr1=arr1, arr2=arr2))
    print(union_arrays_sets(arr1=arr1, arr2=arr2))