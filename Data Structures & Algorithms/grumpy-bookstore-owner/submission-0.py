class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        i, j = 0, 0
        wsum = 0
        while j < minutes:
            if grumpy[j]:
                wsum += customers[j]
            j += 1

        maximum = wsum
        max_i, max_j = i, j

        while j < len(customers):
            if grumpy[j]:
                wsum += customers[j]

            if grumpy[i]:
                wsum -= customers[i]

            i += 1
            j += 1

            if wsum > maximum:
                maximum = wsum
                max_i, max_j = i, j

        result = 0
        for idx in range(len(customers)):
            if max_i <= idx < max_j:
                result += customers[idx]
            elif not grumpy[idx]:
                result += customers[idx]

        return result

        
        