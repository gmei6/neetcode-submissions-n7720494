class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        #prev_small = prices[0]
        curr_small = prices[0]
        
        #prev_large = prices[0]
        curr_large = prices[0]

        for i in range(1, len(prices)):
            print("This is the curr_small: ", curr_small, " and curr_largest: ", curr_large)
            if prices[i] < curr_small:
                profit = curr_large - curr_small
                curr_small = prices[i]
                curr_large = prices[i]
            if prices[i] > curr_large:
                curr_large = prices[i]

        return max(profit, curr_large - curr_small)

        '''
        for i in range(1, len(prices) - 1):
            print("This is the curr_small: ", curr_smallest, " and curr_largest: ", curr_largest)
            if prices[i] < curr_smallest:
                profit = max(profit, curr_largest - curr_smallest)
                curr_smallest = prices[i]
            elif prices[i] > curr_largest:
                profit = max(profit, curr_largest - curr_smallest)
                curr_largest = prices[i]

        return max(profit, curr_largest - curr_smallest)
        '''