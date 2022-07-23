"""  
buy-sell stock
    [7, 1, 5, 3, 6, 4] => 5
    [9, 7, 6, 4, 3, 1] => 0
"""

def max_profit(prices):
    cur_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i-1])
        max_so_far = max(max_so_far , cur_max)
    return max_so_far


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
