class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax = 0
        maxsum = nums[0]
        currmin = 0
        minsum = nums[0]
        totalsum = 0
        for i in range(len(nums)):
            totalsum+= nums[i]
# find the max in liner arry case 1
            currmax+=nums[i]
            if currmax>maxsum:
                maxsum = currmax
            if currmax< 0:
                currmax = 0
# find min in the circular arry case 2
            currmin +=nums[i]
            if currmin<minsum:
                minsum = currmin
            if currmin>0:
                currmin = 0

        # neegative values
        if totalsum == minsum:
            return maxsum
        
        if maxsum > (totalsum-minsum):
            return maxsum
        else:
            return totalsum - minsum
    