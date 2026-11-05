class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        # def quickSearch(left, right):
        #     p, pivot = left, nums[right]
        #     for i in range(left, right):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
                
        #     nums[p], nums[right] = nums[right], nums[p]

        #     if p < k: return quickSearch(p+1, right)
        #     elif p > k: return quickSearch(left, p-1)
        #     else: return nums[p]
        
        # return quickSearch(0, len(nums) - 1)
        left, right = 0, len(nums) - 1
        while left <= right:
            p, pivot = left, nums[right]
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p < k: left = p + 1
            elif p > k: right = p - 1
            else: return nums[p]
        
        return -1
        