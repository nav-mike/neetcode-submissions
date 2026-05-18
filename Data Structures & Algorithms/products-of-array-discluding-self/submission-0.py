class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        preffix = [0] * n
        suffix = [0] * n

        preffix[0] = suffix[n - 1] = 1

        for i in range(1, n):
            preffix[i] = preffix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(n):
            result[i] = suffix[i] * preffix[i]
        
        return result
