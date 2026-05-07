class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n2 = set(nums)
        if len(nums) != len(set(nums)):
            return True
        return False
        