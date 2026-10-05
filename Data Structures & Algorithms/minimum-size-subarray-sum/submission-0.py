class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minimum = float('inf') 
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                minimum = min(right-left+1,minimum)
                total-=nums[left]
                left+=1
        return 0 if minimum == float('inf') else minimum
