"""  
    tow sum
        [2, 7, 11, 15] , 9 = =>[1, 2] 
"""

def tow_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1, p2] # index
            # return [p1 + 1 , p2 + 1] # index + 1
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 + 1


if __name__ == '__main__':
    print(tow_sum([2, 7, 11, 15], 18))
