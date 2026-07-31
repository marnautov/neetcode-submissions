class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        
        i, j = 0, k - 1
        window_sum = sum(arr[i:j + 1])

        while j < len(arr):
            if window_sum >= threshold * k:
                count += 1
            
            j += 1
            
            if j < len(arr):
                window_sum += arr[j]
                window_sum -= arr[i]
                i += 1

        return count
        