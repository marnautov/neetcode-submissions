class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        n = len(code)

        if k == 0:
            return [0] * n

        if k > 0:
            i, j = 1, k
            window_sum = sum(code[1:k + 1])
        else:
            i, j = n + k, n - 1
            window_sum = sum(code[k:])

        while len(result) < n:
            result.append(window_sum)

            window_sum -= code[i % n]
            i += 1
            j += 1
            window_sum += code[j % n]

        return result

        
