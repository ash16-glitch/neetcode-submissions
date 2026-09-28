class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currcount = 0
        maxcount = 0
        for num in nums:
            if num==1:
                currcount+=1
                maxcount = max(maxcount,currcount)
            else:
                currcount = 0
        return maxcount