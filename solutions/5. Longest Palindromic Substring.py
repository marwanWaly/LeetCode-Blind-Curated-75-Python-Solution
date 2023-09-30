class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def max_palindromic(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                
                l -= 1
                r += 1

        for i in range(len(s)):
            # for odd lenght palindromic
            max_palindromic(i ,i)

            # for even lenght palindromic
            max_palindromic(i ,i + 1)
    
        return res
