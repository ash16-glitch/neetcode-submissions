class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                choice1 = s[l+1 : r+1]
                choice2 = s[l : r]
                return (choice1==choice1[::-1]) or (choice2==choice2[::-1])

            l+=1
            r-=1
        return True       