class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = ''.join(c for c in s if c.isalnum()).lower()
        s2 = s1[::-1]

        print(s1,s2)
        if s1==s2:
            return True
        else:
            return False
