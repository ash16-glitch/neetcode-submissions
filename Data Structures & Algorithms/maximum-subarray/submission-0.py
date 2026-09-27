class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum > maxsum:
                maxsum = currsum
            if currsum<0:
                currsum = 0

        return maxsum
