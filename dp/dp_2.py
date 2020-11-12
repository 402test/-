from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(L):
            first,second = 0,0
            for i in L:
                first, second = second,max(i+first,second)
            return second
        return max(help(nums[1:]),help(nums[:-1])) if len(nums) != 1 else nums[0]