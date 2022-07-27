"""  
    remove min 
    [4, 5, 6, 7, 8, -2, 1]
"""

def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:
        return stack

    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storage_stack.append(val)
    
    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min:
            stack.append(val)
    
    return stack, min


if __name__ == '__main__':
    print(remove_min([4, 5, 6, 7, 8, -2, 1]))
