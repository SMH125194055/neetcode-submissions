class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s.lower():
            if i.isalnum():
                ss = ss + i
        # print(ss)
        # print(ss[::-1])
        if ss == ss[::-1]:
           return True
        return False    
