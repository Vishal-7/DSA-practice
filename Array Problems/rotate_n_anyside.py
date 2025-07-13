from typing import List

def rotate_anyside(arr: List[int], side: str, rotate: int) -> List[int]:
    """
    \n Description: Function used to rotate the array to any side given a rotation number \n
    \n Input: array; side; rotate; \n
    \n Output: array after the said rotation \n
    \n Time Complexity: O(n) \n
    """
    n = len(arr)
    rotate %= len(arr) # done to find the number of actual rotations to be made

    if side == "left":
        arr_rotate = arr[:rotate]
        arr = arr[rotate:] + arr_rotate
    else:
        rotate *= -1
        arr_rotate = arr[rotate:]
        arr = arr_rotate + arr[:rotate]
    return arr

def rotate_anyside_reversing(arr: List[int], side: str, rotate: int) -> List[int]:
    """
    \n Description: Function to rotate the array by reversing the elements \n
    \n Input: array; side; rotate; \n
    \n Output: array after rotation \n
    \n Time Complexity: O(n) \n
    """
    n = len(arr)
    rotate %= n

    if side == "left":
        arr[:rotate] = arr[:rotate][::-1]
        arr[rotate:] = arr[rotate:][::-1]
        arr[:] = arr[::-1]
    else:
        arr[-rotate:] = arr[-rotate:][::-1]
        arr[:-rotate] = arr[:-rotate][::-1]
        arr[:] = arr[::-1]
    return arr

if __name__ == "__main__":
    arr = [3,7,8,9,10,11]
    rotate = 3
    side = "left"
    print(rotate_anyside(arr=arr, side=side, rotate=rotate))

    print(f"Rotating a list through reversing the elements inside it.")

    print(rotate_anyside_reversing(arr=arr, side=side, rotate=rotate))