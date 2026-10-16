class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                c1 = s[l+1:r+1]
                c2 = s[l:r]
                return (c1==c1[::-1])or (c2==c2[::-1])
            l+=1
            r-=1
        return True