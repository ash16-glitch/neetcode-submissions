class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s) -1
        for l in range(len(s)):
            if r>l:
                s[r],s[l] = s[l],s[r]
                l+=1
                r-=1
      
        return s

