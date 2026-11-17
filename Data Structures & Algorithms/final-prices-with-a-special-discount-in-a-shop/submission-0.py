class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Brute-force solution (not asymptotically optimal)
        Time: O(n^2), Space: O(n) for result, O(1) auxiliary
        """
        result = []

        for i, num in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= num:
                    result.append(num - prices[j])
                    break
            else:
                result.append(num)

        return result