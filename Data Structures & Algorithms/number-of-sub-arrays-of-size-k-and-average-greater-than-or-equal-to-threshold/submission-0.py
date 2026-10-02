class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        for i in range(len(arr)-k+1):
            maxvalue = 0
            for j in range(i, i+k):
                maxvalue = maxvalue+arr[j]
            if maxvalue / k >= threshold:
                counter+=1
        return counter