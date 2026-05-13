class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()

        for item in nums:
            if hashMap.get(item) is None:
                hashMap[item] = 1
            else:
                return True

        return False
