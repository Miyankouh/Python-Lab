""" 
    Complexity
        Time    Space
    
    big O notation

When solving the algorithm, we must pay attention to the time spent and the amount of resources used
"""
nums = [2, 4, 5, 7, 11, 40, 119]

def show(list, element):
    for i in list:
        if i == element:
            return list.index(i)


print(show(nums, 40))