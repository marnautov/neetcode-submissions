class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = int(window_sum >= threshold * k)

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]

            if window_sum >= threshold * k:
                count += 1

        return count
              