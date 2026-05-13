class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = len(set(nums)) != len(nums)
        return res