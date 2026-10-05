class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxcounter = 0
        for i in range(len(nums)):
            if nums[i]==1:
                counter+=1
                maxcounter = max(counter,maxcounter)
            else:
                counter = 0
        return maxcounter