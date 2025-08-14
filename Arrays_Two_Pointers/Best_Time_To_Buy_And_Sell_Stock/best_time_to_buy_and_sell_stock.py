"""

Best time to buy and sell stock

Description: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints: 1 <= prices.length <= 10^5,0 <= prices[i] <= 10^4

"""

"""

Approaches: 

This is a basic two pointer problem, the prices array can be of length one so I will return 0 if it is length 1. Then I will have the buy pointer starting at index 0 and a sell pointer at index 1. 

Im thinking that we store the lowest number (and its index) reached by the buy pointer and do the same sort of thing for the sell pointer.

So starting both next to each other at the beginning. When the sell pointer is lower than the buy pointer, we move the buy pointer to the sell pointer than move the sell pointer over. If thats not the case we will move the sell pointer to the right continuously to find larger sell values.


My old approach: Worked fine, and is from what I can see the standard approach to this problem, but found a new one that is faster and will study the new one

def buy_sell(prices):
    if len(prices) == 1:
        return 0

    buy = 0
    sell = 1
    max_profit = 0

    while sell != len(prices):
        buy_p = prices[buy]
        sell_p = prices[sell]

        max_profit = max(sell_p - buy_p, max_profit)

        if prices[sell] < prices[buy]:
            buy = sell
        sell += 1
    
    return max_profit

"""

def buy_sell(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices: # setting it up to be managing one element at a time handles the edge case of having a one element length prices array
        if price < min_price: # we only need to store the minimum price, this typically remains fixed, and the price elements checked continuously move to the right
            min_price = price
        elif price - min_price > max_profit: # instead of using the max function which requires more computations, we just do an inequality and store max_profit when the conditional is true
            max_profit = price - min_price

    return max_profit

def main():
    prices = [7,1,5,3,6,4]
    print(buy_sell(prices))

if __name__ == "__main__":
    main()