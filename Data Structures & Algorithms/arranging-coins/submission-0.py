class Solution:
    """
    Greedy simulation.
    
    Time: O(√n)
    Space: O(1)
    """
    def arrangeCoins(self, n: int) -> int:
        level = 1
        
        while n >= level:
            n -= level
            level += 1

        return level - 1