class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for char in s:
            if char.isalnum():
                t+=char
        t = t.lower()
        start = 0
        end = len(t) - 1
        
        while start < end:
            if t[start] != t[end]:
                return False
            start+=1
            end-=1
        return True

                