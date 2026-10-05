class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        s = str(x)
        l = len(s) -1
        while i < l/2:
            if s[i] == s[l-i]:
                i+=1
            else:
                return False
        return True

## answer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]