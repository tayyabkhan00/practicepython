def maxProfit(prices):
    min_price = float('inf')     # 1
    max_profit = 0               # 2

    for price in prices:         # 3
        if price < min_price:    # 4
            min_price = price    # 5

        profit = price - min_price  # 6
        
        if profit > max_profit:     # 7
            max_profit = profit     # 8

    return max_profit              # 9

prices = [7, 1, 5, 3, 6, 4]
