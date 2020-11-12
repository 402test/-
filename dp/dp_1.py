from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size ==1:
            return nums[0]

        dp = [0]*size
        dp[0] = nums[0]
        dp[1] =  max(nums[0], nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])

        return dp[size-1]

# 考虑到 最高金额 只与该房间的前两个房间的最高金额有关  ， 这时可以采用滚动数组

class SolutionSuper:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size ==1:
            return nums[0]

        first,second = nums[0],max(nums[0],nums[1])
        for i in range(2,size):
            first, second = second,max(first+nums[i],second)

        return second








s = SolutionSuper()
print(s.rob([1,2,3,1]))