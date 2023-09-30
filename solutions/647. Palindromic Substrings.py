class Solution:
    res = 0

    def countSubstrings(self, s: str) -> int:
        def count_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                self.res += 1
        
        for i in range(len(s)):

            # for odd palindrome
            count_palindrome(i, i)

            # for even palindrome
            count_palindrome(i, i+1)
            
        return self.res
