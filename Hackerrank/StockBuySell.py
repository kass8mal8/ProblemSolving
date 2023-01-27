def buy_sell_once(prices):
    min_price, max_profit = prices[0], 0.0
    
    for price in prices:
        max_profit_sell = price - min_price
        max_profit = max(max_profit_sell, max_profit)
        min_price = min(min_price, price)

    return max_profit


P = [310, 355, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_sell_once(P))
