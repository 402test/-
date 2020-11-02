'''


给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
'''
#  学习动态规划吧


'''
问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

# 斐波拉且数列
#
# def f(n):
#
#     if n<=2:
#         return n
#
#     i,j = 1,2
#     for k in range(3,n+1):
#         i,j = j,i+j
#     return j
#
#
# print(f(10))



#  动态规划  解决
# def f(n):
#     if n<=2:
#         return n
#     dp = [0,1,2]
#
#
#
#     for i in range(3,n+1):
#
#         k= dp[i-1]+dp[i-2]
#         dp.append(k)
#
#     return dp[n]
#
# print(f(10))



'''


给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小






动态规划思路  


维护一个二维列表

长宽和  给定网格一致  但是初始值 都是 0     [[0]*col for _ in range(row)]

然后算出  到一一行所需要的步数    因为同一行只能向右边走    
然后算出  到一一列所需要的步数    因为同一列只能向下边走  


通过行数 来循环的出到每一行第一个数  所需要的布数
for i in range(1,row):
    dp[i][0] = dp[i-1][0]++grid[i][0]

通过列数（就是第一行的数据长度） 的出 到 第一行的所有节点  需要的 步数


for i in range(1,col):
    dp[0][i] = dp[0][i-1]+grid[0][i]

'''

# f(m,n) = f(m-1,n)+f(m,n-1)
# 力扣版
# from typing import List
#
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#
#         rows,columns = len(grid),len(grid[0])
#
#         dp = [[0] * columns for _ in range(rows)]  # 初始化一个都是  0  的dp 节点
#
#         # 因为 从初始位置到   第一横排  和 第一列 的节点   布数是固定的   所以 得出到 第一排 和 第一列所以节点的 步数
#
#         dp[0][0] = grid[0][0]
#
#         # 第一列 的节点
#         for i in range(1,rows):
#             dp[i][0] = dp[i-1][0]+grid[i][0]
#
#         #第一行的节点
#
#         for j in range(1,columns):
#             dp[0][j] = dp[0][j-1] + grid[0][j]
#
#
#         for i in range(1,rows):
#             for j in range(1,columns):
#                 dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
#
#
#         return dp[rows-1][columns-1]



# 或者 循环合在一起
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        dp = [[0] * columns for _  in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if i ==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i ==0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


