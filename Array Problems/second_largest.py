def second_largest(arr: list) -> int:
    """
    \n Description: Function to find the second largest element \n
    \n Input: Sample array \n
    \n Output: Second largest element \n
    \n Time Complexity: O(n) 
    """
    if len(arr) < 2:
        return -1, -1 # return -1 when the logic cannot find the second largest element
    
    max_ele = arr[0]
    sec_ele = arr[0]

    for i in arr:
        if i > max_ele:
            sec_ele = max_ele
            max_ele = i
        else:
            if i > sec_ele and i != max_ele:
                sec_ele = i
    return (max_ele, sec_ele)

if __name__ == "__main__":
    nums = [1]
    max_ele, sec_ele = second_largest(nums)

    print(f"Largest Element: {max_ele} || Second Largest Element: {sec_ele}")