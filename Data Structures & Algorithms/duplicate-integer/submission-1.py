class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for r in range(len(nums)):
            if nums[r]  in duplicate:
                return True
            duplicate.add(nums[r]) 
             
        return False