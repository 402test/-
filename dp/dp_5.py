

#  暴力迭代
# from typing import List
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         if not rows or not matrix[0]:
#             return 0
#         cols = len(matrix[0])
#         maxSide = 0
        
#         for r in range(rows):
#             for c in range(cols):
#                 if matrix[r][c] =='1':

#                      maxSide = max(maxSide, 1)
#                      currentMaxSide = min(rows - r, cols - c)  #  可能正方形的 最大边长
#                      for k in range(1,currentMaxSide):

#                          flag = True
#                          if matrix[r+k][c+k] =='0':
#                              break
#                          for m in range(k):
                             
#                              if matrix[r+m][c+k] =='0' or  matrix[r+k][c+m]=='0':
#                                  flag =False
#                                  break
#                          if flag:

#                              maxSide = max(maxSide,k+1)
                            
#                          else:
#                              break

#         return maxSide*maxSide

# 动态规划  
# from typing import List
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         if not rows or not matrix[0]:
#             return 0
#         cols = len(matrix[0])
#         maxSide = 0
#         dp = [[0]* cols for _ in range(rows)]
#         for r in range(rows):
#             for c in range(cols):
#                 if matrix[r][c] =='1': 
#                     if r==0 or c ==0:
#                         dp[r][c] = 1
#                     else:
#                         dp[r][c] = min(dp[r-1][c-1],dp[r-1][c],dp[r][c-1])+1
#                 maxSide = max(maxSide,dp[r][c])
#         return maxSide*maxSide


#  动态规划 优化 一维
# from typing import List
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         if not rows or not matrix[0]:
#             return 0
#         cols = len(matrix[0])
#         maxSide = 0
#         dp = [0]*cols
#         for i in range(rows):
#             ndp = [0]*cols
#             for j in range(cols):
#                 if matrix[i][j]=='1':
#                     ndp[j] = 1
#                     if i and j:
#                         ndp[j] = min(ndp[j-1],dp[j],dp[j-1])+1
#             dp = ndp
#             maxSide = max(maxSide,max(ndp))
#         return maxSide*maxSide


#  别人写的  
# from typing import List
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         #动态规划 + 空间优化
#         #时间复杂度：O(mn)
#         #空间复杂度：O(n)
#         if not matrix:
#             return 0
#         res = 0
#         m, n = len(matrix), len(matrix[0])
#         dp = [0] * n
#         prepre = 0
#         for i in range(m):
#             for j in range(n):
#                 temp = dp[j]
#                 if matrix[i][j] == '1':
#                     if i== 0 or j == 0:
#                         dp[j] = 1
#                     else:    
#                         dp[j] = min(dp[j], dp[j-1], prepre ) + 1
#                 else:
#                     dp[j] = 0
#                 res = max(res, dp[j])
#                 prepre = temp
#             #print(i, dp)
#         return res * res


s = Solution()
print(s.maximalSquare(
[["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]]))