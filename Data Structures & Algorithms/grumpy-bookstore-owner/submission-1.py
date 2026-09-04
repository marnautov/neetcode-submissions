class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        extra = 0

        for idx in range(len(customers)):
            if grumpy[idx] == 0:
                satisfied += customers[idx]

        for idx in range(minutes):
            if grumpy[idx] == 1:
                extra += customers[idx]

        max_extra = extra
        for right in range(minutes, len(customers)):
            if grumpy[right] == 1:
                extra += customers[right]

            left = right - minutes

            if grumpy[left] == 1:
                extra -= customers[left]

            max_extra = max(extra, max_extra)

        return satisfied + max_extra

            