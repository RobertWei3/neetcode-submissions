class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for buy in range(len(prices)- 1):
        #     sell = buy + 1
        #     while sell < (len(prices) -1) and prices[sell] > prices[buy]:
        #         curr_profit = prices[sell] - prices[buy]
        #         max_profit = max(curr_profit, max_profit)
        #         sell += 1

        # return max_profit

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r

            r += 1
        return max_profit



