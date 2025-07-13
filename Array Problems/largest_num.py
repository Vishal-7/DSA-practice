def largest_number(arr:list) -> int:
    """
    \n Description: Function to find the largest number in a list \n
    \n Input: array \n
    \n Outout: largest number in the array \n
    \n Time Complexity: O(n)
    """
    if len(arr) == 1:
        return arr[0]
    else:
        max_element = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_element:
                max_element = arr[i]
        return max_element

if __name__ == "__main__":
    print(largest_number([2,5,1,3,0]))