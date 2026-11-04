class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for w in s:
            if w.isalnum():
                ss += w.lower()
        return ss == ss[::-1]