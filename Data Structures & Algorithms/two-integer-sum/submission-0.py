class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()

        for idx in range(0, len(nums)):
            val = target - nums[idx]
            if val in hashMap:
                return [hashMap[val], idx]
            
            hashMap[nums[idx]] = idx
        
        return [-1, -1]