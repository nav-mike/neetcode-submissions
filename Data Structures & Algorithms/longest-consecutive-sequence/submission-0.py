class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        buffer = {}
        result = 0
        for n in nums:
            buffer[n] = True
        
        for idx, n in enumerate(nums):
            if n - 1 in buffer:
                continue
            
            count = 1
            val = n
            while (val + 1) in buffer:
                count += 1
                val += 1
                print(count, val, result)
                result = max(result, count)

        return result