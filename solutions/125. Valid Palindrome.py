class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            if not self.is_alphanumeric(s[l]):
                l += 1
                continue
            
            if not self.is_alphanumeric(s[r]):
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
    
    def is_alphanumeric(self, c):
        return ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")
