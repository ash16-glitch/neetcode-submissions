class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxcounter = 0
        for num in nums:
            if num ==1:
                current +=1
                if current>maxcounter:
                    maxcounter = current       
            else:
                current = 0
        return maxcounter