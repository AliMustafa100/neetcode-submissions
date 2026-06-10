class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = ''.join(c for c in s if c.isalnum()).lower() #cleaned string , return c for c in string if c is alphanum or c is a whitespace
        s1 = s2[::-1] #reverse that clean list 

        print(s1)

        if s1 == s2:
            return True
        else:
            return False