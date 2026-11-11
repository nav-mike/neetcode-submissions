class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return [[]]

        perms = self.permute(nums[1:])
        result = []

        for p in perms:
            for i in range(0, len(p) + 1):
                tmp = p.copy()
                tmp.insert(i, nums[0])
                result.append(tmp)

        return result