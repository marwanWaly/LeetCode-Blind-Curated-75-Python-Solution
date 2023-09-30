class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count_palindrome(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
        for i in range(len(s)):

            # for odd palindrome
            count_palindrome(i, i)

            # for even palindrome
            count_palindrome(i, i+1)
            
        return res
