class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # dictionary
        l = 0 # left pointer
        res = 0 # holds the result with maximum char
        for r in range(len(s)): # loop through the string 
            if s[r] in count:
                count[s[r]] = 1 + count[s[r]]
            else:
                count[s[r]] = 1 + 0
            while (r-l+1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res

            

        