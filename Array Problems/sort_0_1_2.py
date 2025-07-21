from typing import List

def sort_nums(arr: List[int]) -> List:
    """
    \n Description: Function to sort the numbers (0, 1, 2) in numerical order \n
    \n Input: unsorted array \n
    \n Output: sorted array \n
    \n Time Complexity: O(n) \n
    """
    cnt_0, cnt_1, cnt_2 = 0, 0, 0

    for num in arr:
        if num == 0:
            cnt_0 += 1
        elif num == 1:
            cnt_1 += 1
        elif num == 2:
            cnt_2 += 1
    # print(cnt_0, cnt_1, cnt_2)

    for i in range(cnt_0):
        arr[i] = 0
    for j in range(cnt_0, cnt_0+cnt_1):
        arr[j] = 1
    for k in range(cnt_0+cnt_1, cnt_0+cnt_1+cnt_2):
        arr[k] = 2
    return arr

if __name__ == "__main__":
    print(sort_nums([0]))