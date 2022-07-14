"""  
    Constant Time o(1)

    A lot of data does not affect the speed
"""

nums = [3, 4, 6, 98, 123, 42, 6432]


def show(list):
    if list[0] % 2 == 0:
        return 'Even'
    return 'odd'


if __name__ == '__main__':
    print(show(nums))