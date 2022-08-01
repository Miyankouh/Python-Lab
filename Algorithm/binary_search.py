"""  
    binary search 
        [2, 3, 4, 6, 12, 19, 20, 21], 12 => 5
"""

def binary_search(array, element):
    low, high = 0, len(array)-1

    while low <= high:
        mid  = (high + low) // 2
        val = array[mid]
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    print(binary_search([2, 3, 4, 6, 12, 19, 20, 21], 4))  # index[2]
    print(binary_search([2, 3, 4, 6, 12, 19, 20, 21], 12)) # index[4]
    print(binary_search([2, 3, 4, 6, 12, 19, 20, 21], 21)) # index[7]
