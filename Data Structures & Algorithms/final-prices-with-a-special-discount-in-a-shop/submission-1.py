class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Monotonic increasing stack.
        Time: O(n); Space: O(n) auxiliary.
        """
        stack: List[int] = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                prices[idx] = prices[idx] - price
            
            stack.append(i)

        return prices