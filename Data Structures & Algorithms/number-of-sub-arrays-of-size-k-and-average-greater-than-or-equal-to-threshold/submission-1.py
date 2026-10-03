class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        l = 0
        maxv = 0
        for r in range(len(arr)):
            maxv = maxv+arr[r]            
            if r-l+1>k:
                maxv = maxv-arr[l]
                l+=1    
            if r - l + 1 == k:
                if maxv/k >= threshold:
                    counter+=1

            
        return counter