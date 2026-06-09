
        
        #declare a hashmap for tracking consecutives
        #nvm declare a set to see if this num in set for 0(1) time
      #add number if that number equal to that number plus 1 
        #if not break and start a new key
        # return lenght 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num2 = set(nums)  #  nums(set) → set(nums)
        longest = 0

        for num in num2:
            if num - 1 not in num2:
                current = num
                length = 1

                while current + 1 in num2:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest




        